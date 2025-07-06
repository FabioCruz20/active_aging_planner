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
