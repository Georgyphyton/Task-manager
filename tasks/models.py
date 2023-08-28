from django.db import models
from statuses.models import Statuses
from users.models import CustomUser
from labels.models import Labels


class Tasks(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, verbose_name='Статус')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    executor = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Исполнитель',
                                 related_name='executer', null=True, blank=True)
    labels = models.ManyToManyField(Labels, through='Relations', blank=True, verbose_name="Метки")

    def __str__(self):
        return self.name


class Relations(models.Model):
    labels = models.ForeignKey(Labels, on_delete=models.PROTECT)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)
