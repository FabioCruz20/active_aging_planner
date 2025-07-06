from django.shortcuts import render, redirect
from planning.models import Level
from planning.forms import LevelForm

def list_view(request):
    '''
    '''
    levels = Level.objects.all()
    return render(request, 'levels/index.html', { 'levels': levels })


def new_view(request):
    '''
    '''
    if request.method == 'POST':
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('levels:list')        
    else:
        form = LevelForm()
    
    return render(request, 'levels/create.html', { 'form': form })


def edit_view(request, level_id):
    '''
    '''
    level = Level.objects.get(id = level_id)
    if level is None:
        return redirect('levels:list')
    
    if request.method == 'POST':
        form = LevelForm(request.POST, instance = level)
        if form.is_valid():
            form.save()
            return redirect('levels:list')
    else:
        form = LevelForm(instance = level)
    
    return render(request, 'levels/edit.html', { 'form': form })


def delete(request, level_id):
    '''
    '''
    level = Level.objects.get(id = level_id)
    if level:
        level.delete()
    
    return redirect('levels:list')
