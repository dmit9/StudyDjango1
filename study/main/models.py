from asyncio import tasks
from tabnanny import verbose
from turtle import title
from django.db import models

class TaskTable(models.Model):
    title = models.CharField('Квартира', max_length=20)
    task = models.TextField('Месяц')
##   many = models.IntegerField('Деньги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уборка'
        verbose_name_plural = 'Уборки'
