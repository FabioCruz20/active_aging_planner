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
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full mb-4'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full mb-4'
            }),
        }


class LevelForm(forms.ModelForm):
    '''
    '''
    class Meta:
        model = models.Level
        fields = ['level_number', 'name', 'description']
        widgets = {
            'level_number': forms.NumberInput(attrs={
                'class': 'block w-full mb-4'
            }),
            'name': forms.TextInput(attrs={
                'class': 'block w-full mb-4'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full mb-4'
            }),
        }   


ProjectLevelFormSet = forms.inlineformset_factory(
    models.Project, 
    models.ProjectLevel,
    fields=['level', 'progress_percentage'],
    widgets={
        'level': forms.Select(attrs={'class': 'w-full'}),
        'progress_percentage': forms.NumberInput(attrs={'class': ''}),
    },
    extra=1,
    can_delete=True,
)

ProjectLevelActionFormSet = forms.inlineformset_factory(
    models.ProjectLevel,
    models.ProjectLevelAction,
    fields=['action'],
    widgets={
        'action': forms.Select(attrs={'class': 'w-full'})
    },
    extra=1,
    can_delete=True,
)