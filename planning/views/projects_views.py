from django.shortcuts import render, redirect, get_object_or_404
from planning import models
from planning import forms

# Create your views here.

def list_view(request):
    '''
    '''
    projects = models.Project.objects.all()
    return render(request, 'projects/index.html', { 'projects': projects })


def new_view(request):
    '''
    '''
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            # processa e redireciona.
            form.save()
            return redirect('projects:list')
    else:
        form = forms.ProjectForm()

    return render(request, 'projects/create.html', { 'form': form })


def edit_view(request, project_id):
    '''
    '''
    project = models.Project.objects.get(id=project_id)
    if project is None:
        return redirect('projects:list')

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, instance=project)
        if form.is_valid():
            # processa e redireciona.
            form.save()
            return redirect('projects:list')
    else:
        form = forms.ProjectForm(instance=project)

    return render(request, 'projects/edit.html', { 'form': form })


def delete(request, project_id):
    '''
    '''
    project = models.Project.objects.get(id=project_id)
    if project:
        project.delete()

    return redirect('projects:list')
    

def manage_project_levels_view(request, project_id):
    ''''''

    project = get_object_or_404(models.Project, pk=project_id)

    if request.method == 'POST':
        formset = forms.ProjectLevelFormSet(request.POST, instance=project)

        if formset.is_valid():
            formset.save()
            return redirect('projects:manage_levels', project_id=project_id)
    else:
        formset = forms.ProjectLevelFormSet(instance=project)

    context = {
        'project': project,
        'level_formset': formset,
    }
    return render(request, 'projects/manage_levels.html', context)


def manage_level_actions_view(request, projectlevel_id):
    ''''''

    project_level = get_object_or_404(models.ProjectLevel, pk=projectlevel_id)

    if request.method == 'POST':
        formset = forms.ProjectLevelActionFormSet(request.POST, instance=project_level)
        if formset.is_valid():
            formset.save()
            return redirect('projects:manage_actions', projectlevel_id=projectlevel_id)
    else:
        formset = forms.ProjectLevelActionFormSet(instance=project_level)
    
    context = {
        'project_level': project_level,
        'action_formset': formset,
    }
    return render(request, 'projects/manage_actions.html', context)


def manage_actions_matrix_view(request, project_id):
    '''
    View para gerenciar ações usando uma matriz de Eixos x Níveis
    '''
    project = get_object_or_404(models.Project, pk=project_id)
    
    # Buscar todos os eixos e níveis
    axes = models.Axis.objects.all()
    levels = models.Level.objects.all().order_by('level_number')
    
    # Criar matriz de ações organizadas por eixo e nível
    matrix = {}
    for axis in axes:
        matrix[axis] = {}
        for level in levels:
            # Buscar ações para este eixo e nível
            actions = models.Action.objects.filter(axis=axis, level=level)
            
            # Buscar progresso atual para este projeto, eixo e nível
            try:
                project_level_axis = models.ProjectLevelAxis.objects.get(
                    project=project, axis=axis, level=level
                )
                progress = project_level_axis.progress_percentage
            except models.ProjectLevelAxis.DoesNotExist:
                progress = 0
                
            matrix[axis][level] = {
                'actions': actions,
                'progress': progress
            }
    
    if request.method == 'POST':
        # Processar atualizações de progresso
        for axis in axes:
            for level in levels:
                progress_key = f'progress_{axis.id}_{level.id}'
                if progress_key in request.POST:
                    progress_value = float(request.POST[progress_key])
                    
                    # Criar ou atualizar ProjectLevelAxis
                    project_level_axis, created = models.ProjectLevelAxis.objects.get_or_create(
                        project=project,
                        axis=axis,
                        level=level,
                        defaults={'progress_percentage': progress_value}
                    )
                    
                    if not created:
                        project_level_axis.progress_percentage = progress_value
                        project_level_axis.save()
        
        return redirect('projects:manage_actions_matrix', project_id=project_id)
    
    context = {
        'project': project,
        'axes': axes,
        'levels': levels,
        'matrix': matrix,
    }
    return render(request, 'projects/manage_actions_matrix.html', context)


def manage_axis_level_actions_view(request, project_id, axis_id, level_id):
    '''
    View para gerenciar ações específicas de uma combinação eixo/nível
    '''
    project = get_object_or_404(models.Project, pk=project_id)
    axis = get_object_or_404(models.Axis, pk=axis_id)
    level = get_object_or_404(models.Level, pk=level_id)
    
    # Buscar todas as ações já adicionadas para este eixo e nível
    added_actions = models.Action.objects.filter(axis=axis, level=level)
    
    # Buscar ações disponíveis que ainda não foram adicionadas
    # (ações únicas de outros projetos para a mesma combinação eixo/nível)
    all_possible_actions = models.Action.objects.filter(
        axis=axis, 
        level=level
    ).values('name').distinct().order_by('name')
    
    # Filtrar apenas as ações que ainda não foram adicionadas
    added_action_names = set(added_actions.values_list('name', flat=True))
    available_actions_to_add = [
        action for action in all_possible_actions 
        if action['name'] not in added_action_names
    ]
    
    # Buscar ou criar ProjectLevelAxis para este projeto, eixo e nível
    project_level_axis, created = models.ProjectLevelAxis.objects.get_or_create(
        project=project,
        axis=axis,
        level=level,
        defaults={'progress_percentage': 0}
    )
    
    if request.method == 'POST':
        selected_action_name = request.POST.get('selected_action_name')
        action_id = request.POST.get('action_id')
        
        if 'add_action' in request.POST and selected_action_name:
            # Verificar se a ação já existe para evitar duplicatas
            existing_action = models.Action.objects.filter(
                name=selected_action_name, axis=axis, level=level
            ).first()
            
            if not existing_action:
                models.Action.objects.create(
                    name=selected_action_name,
                    axis=axis,
                    level=level
                )
            
            return redirect('projects:manage_axis_level_actions', 
                          project_id=project_id, axis_id=axis_id, level_id=level_id)
        
        elif 'delete_action' in request.POST and action_id:
            # Remover ação
            action = get_object_or_404(models.Action, pk=action_id)
            if action.axis == axis and action.level == level:
                action.delete()
            return redirect('projects:manage_axis_level_actions', 
                          project_id=project_id, axis_id=axis_id, level_id=level_id)
    
    context = {
        'project': project,
        'axis': axis,
        'level': level,
        'added_actions': added_actions,
        'available_actions_to_add': available_actions_to_add,
        'project_level_axis': project_level_axis,
    }
    return render(request, 'projects/manage_axis_level_actions.html', context)
