from django.shortcuts import render, redirect, get_object_or_404
from planning import models
from planning import forms


def manage_actions_matrix_view(request):
    '''
    View para gerenciar ações usando uma matriz de Eixos x Níveis
    '''
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
            
            # Buscar ProjectActions e suas tarefas para calcular o progresso
            project_actions = models.ProjectAction.objects.filter(
                axis=axis,
                level=level
            ).select_related('action')
            
            total_actions = project_actions.count()
            completed_actions = 0
            
            for project_action in project_actions:
                tasks = models.Task.objects.filter(project_action=project_action)
                total_tasks = tasks.count()
                completed_tasks = tasks.filter(status='DONE').count()
                
                # Se todas as tarefas da ação estão concluídas, incrementa o contador
                if total_tasks > 0 and total_tasks == completed_tasks:
                    completed_actions += 1
            
            # Calcular a porcentagem de progresso
            progress = (completed_actions / total_actions * 100) if total_actions > 0 else 0
            
            matrix[axis][level] = {
                'actions': actions,
                'progress': progress,
                'total_actions': total_actions,
                'completed_actions': completed_actions,
                'project_actions': project_actions
            }
    
    context = {
        'axes': axes,
        'levels': levels,
        'matrix': matrix,
    }
    return render(request, 'projects/manage_actions_matrix.html', context)


def manage_level_actions_view(request, projectlevel_id):
    '''
    View para gerenciar ações de um nível específico
    '''
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





def manage_tasks_view(request, project_action_id):
    '''
    View para gerenciar tarefas de uma ação específica do projeto
    '''
    project_action = get_object_or_404(models.ProjectAction, pk=project_action_id)
    tasks = models.Task.objects.filter(project_action=project_action).order_by('-created_at')
    
    # Calcular estatísticas
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='DONE').count()
    progress_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    context = {
        'project_action': project_action,
        'action': project_action.action,
        'axis': project_action.axis,
        'level': project_action.level,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress_percentage': progress_percentage,
        'status_choices': models.Task.STATUS_CHOICES,
    }
    return render(request, 'projects/manage_tasks.html', context)


def create_task_view(request, project_action_id):
    '''
    View para criar uma nova tarefa
    '''
    project_action = get_object_or_404(models.ProjectAction, pk=project_action_id)
    
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project_action = project_action
            task.save()
            return redirect('projects:manage_tasks', project_action_id=project_action_id)
    else:
        form = forms.TaskForm()
    
    context = {
        'form': form,
        'project_action': project_action,
        'action': project_action.action,
    }
    return render(request, 'projects/create_task.html', context)


def edit_task_view(request, task_id):
    '''
    View para editar uma tarefa existente
    '''
    task = get_object_or_404(models.Task, pk=task_id)
    project_action = task.project_action
    
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('projects:manage_tasks', project_action_id=project_action.id)
    else:
        form = forms.TaskForm(instance=task)
    
    context = {
        'form': form,
        'task': task,
        'project_action': project_action,
        'action': project_action.action,
    }
    return render(request, 'projects/edit_task.html', context)


def delete_task_view(request, task_id):
    '''
    View para excluir uma tarefa
    '''
    task = get_object_or_404(models.Task, pk=task_id)
    project_action_id = task.project_action.id
    task.delete()
    return redirect('projects:manage_tasks', project_action_id=project_action_id)


def manage_axis_level_actions_view(request, axis_id, level_id):
    '''
    View para gerenciar ações específicas de uma combinação eixo/nível
    '''
    axis = get_object_or_404(models.Axis, pk=axis_id)
    level = get_object_or_404(models.Level, pk=level_id)
    
    # Buscar todas as ações já adicionadas para este eixo e nível
    project_actions = models.ProjectAction.objects.filter(
        axis=axis, level=level
    ).select_related('action')
    added_actions = [pa.action for pa in project_actions]
    
    # Buscar ações disponíveis que ainda não foram adicionadas
    # (ações únicas para a mesma combinação eixo/nível)
    all_possible_actions = models.Action.objects.filter(
        axis=axis, 
        level=level
    ).distinct().order_by('name')
    
    # Filtrar apenas as ações que ainda não foram adicionadas
    added_action_names = set([action.name for action in added_actions])
    available_actions_to_add = [
        action for action in all_possible_actions 
        if action.name not in added_action_names
    ]
    
    # Buscar ou criar ProjectLevelAxis para este eixo e nível
    project_level_axis, created = models.ProjectLevelAxis.objects.get_or_create(
        axis=axis,
        level=level,
        defaults={'progress_percentage': 0}
    )
    
    if request.method == 'POST':
        selected_action_name = request.POST.get('selected_action_name')
        custom_action_name = request.POST.get('custom_action_name')
        project_action_id = request.POST.get('project_action_id')
        
        if 'add_action' in request.POST:
            action_name = selected_action_name if selected_action_name != 'custom' else custom_action_name
            
            if action_name:
                # Buscar ou criar a ação
                action, created = models.Action.objects.get_or_create(
                    name=action_name,
                    axis=axis,
                    level=level
                )
                
                # Criar o vínculo com a ação (se não existir)
                models.ProjectAction.objects.get_or_create(
                    action=action,
                    axis=axis,
                    level=level
                )
            
            return redirect('projects:manage_axis_level_actions', 
                          axis_id=axis_id, level_id=level_id)
        
        elif 'delete_action' in request.POST and project_action_id:
            # Remover apenas o vínculo com a ação (não a ação em si)
            project_action = get_object_or_404(models.ProjectAction, pk=project_action_id)
            if project_action.axis == axis and project_action.level == level:
                project_action.delete()
            return redirect('projects:manage_axis_level_actions', 
                          axis_id=axis_id, level_id=level_id)
    
    context = {
        'axis': axis,
        'level': level,
        'added_actions': added_actions,
        'project_actions': project_actions,
        'available_actions_to_add': available_actions_to_add,
        'project_level_axis': project_level_axis,
    }
    return render(request, 'projects/manage_axis_level_actions.html', context)
