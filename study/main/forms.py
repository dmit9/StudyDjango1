##from dataclasses import fields
from .models import TaskTable
from django.forms import ModelForm, TextInput, Textarea


class TaskTableForm(ModelForm):
    class Meta:
        model = TaskTable
        fields = ['title', 'task']
        widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ввести кв'
        }),
        "task": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ввести месяц'
        }),
            }
