from django import forms
from . import models


class ActionForm(forms.ModelForm):
    '''
    '''
    class Meta:
        model = models.Action
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full mb-4'
            }),
        }


class LevelForm(forms.ModelForm):
    '''
    '''
    class Meta:
        model = models.Level
        fields = ['level_number', 'name']
        widgets = {
            'level_number': forms.NumberInput(attrs={
                'class': 'block w-full mb-4'
            }),
            'name': forms.TextInput(attrs={
                'class': 'block w-full mb-4'
            }),
        }   


class TaskForm(forms.ModelForm):
    '''
    Formulário para criar e editar tarefas
    '''
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
                'rows': 4
            }),
            'status': forms.Select(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
        }


class PaperForm(forms.ModelForm):
    '''
    Formulário para criar e editar artigos científicos
    '''
    class Meta:
        model = models.Paper
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'url': forms.URLInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'
            }),
        }

