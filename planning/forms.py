from django import forms
from . import models

class ProjectForm(forms.ModelForm):
    '''
    '''
    class Meta:
        model = models.Project
        fields = ['name', 'description'] 
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full mb-4'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full mb-4'
            }),
        }   


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

