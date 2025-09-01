from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from planning import forms
from planning import models


def list_papers(request):
    '''
    View para listar artigos científicos
    '''
    papers = models.Paper.objects.all().order_by('-created_at')
    context = {
        'papers': papers
    }
    return render(request, 'papers/index.html', context)


def create_paper(request):
    '''
    View para criar um novo artigo científico
    '''
    if request.method == 'POST':
        form = forms.PaperForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artigo criado com sucesso!')
            return redirect('papers:index')
    else:
        form = forms.PaperForm()

    context = {
        'form': form
    }
    return render(request, 'papers/create.html', context)


def edit_paper(request, paper_id):
    '''
    View para editar um artigo científico
    '''
    paper = get_object_or_404(models.Paper, pk=paper_id)

    if request.method == 'POST':
        form = forms.PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artigo atualizado com sucesso!')
            return redirect('papers:index')
    else:
        form = forms.PaperForm(instance=paper)

    context = {
        'form': form,
        'paper': paper
    }
    return render(request, 'papers/edit.html', context)


def delete_paper(request, paper_id):
    '''
    View para excluir um artigo científico
    '''
    paper = get_object_or_404(models.Paper, pk=paper_id)

    if request.method == 'POST':
        paper.delete()
        messages.success(request, 'Artigo excluído com sucesso!')
        return redirect('papers:index')

    context = {
        'paper': paper
    }
    return render(request, 'papers/delete.html', context)