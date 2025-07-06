from django.shortcuts import render, redirect
from planning.models import Action
from planning.forms import ActionForm

def list_view(request):
    '''
    '''
    actions = Action.objects.all()
    return render(request, 'actions/index.html', { 'actions': actions })


def new_view(request):
    '''
    '''
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actions:list')        
    else:
        form = ActionForm()
    
    return render(request, 'actions/create.html', { 'form': form })


def edit_view(request, action_id):
    '''
    '''
    action = Action.objects.get(id = action_id)
    if action is None:
        return redirect('actions:list')
    
    if request.method == 'POST':
        form = ActionForm(request.POST, instance = action)
        if form.is_valid():
            form.save()
            return redirect('actions:list')
    else:
        form = ActionForm(instance = action)
    
    return render(request, 'actions/edit.html', { 'form': form })


def delete(request, action_id):
    '''
    '''
    action = Action.objects.get(id = action_id)
    if action:
        action.delete()
    
    return redirect('actions:list')
