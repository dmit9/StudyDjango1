from dataclasses import fields
from .models import TaskTable
from django.forms import ModelForm


class TaskTableForm(ModelForm):
    class Meta:
        model = TaskTable
        fields = ['title', 'task']
