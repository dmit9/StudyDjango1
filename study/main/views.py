from multiprocessing import context
from django.shortcuts import render
#from django.http import HttpResponse
from .models import TaskTable
from .forms import TaskTableForm


def index(reguest):
    tasksList = TaskTable.objects.order_by('id')
    return render(reguest, 'main/index.html', {'title': 'Главная страница сайта', 'taskList':tasksList})

def about(reguest):
    return render(reguest, "main/about.html")

def create(reguest):
    form = TaskTableForm()
    context = {
        'form': form
    }
    return render(reguest, "main/create.html")
