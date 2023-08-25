from django.db import models


class Statuses(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="имя")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
