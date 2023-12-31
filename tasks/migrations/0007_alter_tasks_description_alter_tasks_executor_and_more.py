# Generated by Django 4.2.4 on 2023-08-28 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0002_alter_labels_name'),
        ('statuses', '0005_alter_statuses_name'),
        ('tasks', '0006_relations_tasks_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Executor'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.Relations', to='labels.labels', verbose_name='Labels'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.statuses', verbose_name='Status'),
        ),
    ]
