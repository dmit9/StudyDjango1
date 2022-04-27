from multiprocessing import context
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import TaskTable
from .forms import TaskTableForm


def index(reguest):
    tasksList = TaskTable.objects.order_by('id')
    return render(reguest, 'main/index.html', {'title': 'Главная страница сайта', 'taskList':tasksList})

def about(reguest):
    return render(reguest, "main/about.html")

def create(reguest):
    error = ''
    if reguest.method == 'POST':
        form = TaskTableForm(reguest.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна!'

    form = TaskTableForm()
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, "main/create.html", context)
