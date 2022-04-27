from dataclasses import fields
from .models import TaskTable
from django.forms import ModelForm


class TaskTable(ModelForm):
    class Meta:
        model = TaskTable
        fields = ['title', 'task']
