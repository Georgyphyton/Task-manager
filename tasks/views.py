from django.views.generic import DetailView
from django.urls import reverse_lazy
from tasks.models import Tasks
from tasks.forms import CreateTaskForm, SearchFilter
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.mixins import CustomLoginRequiredMixin, TaskOwnerMixin
from django_filters.views import FilterView


class IndexView(CustomLoginRequiredMixin, FilterView):

    filterset_class = SearchFilter
    model = Tasks
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'


class TaskView(CustomLoginRequiredMixin, DetailView):

    model = Tasks
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class CreateTaskView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateTaskForm
    model = Tasks
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = "Задача добавлена"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskEditView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateTaskForm
    model = Tasks
    template_name = 'tasks/update.html'
    success_message = "Задача изменена"
    success_url = reverse_lazy('tasks')


class TaskDeleteView(TaskOwnerMixin, CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = "Задача успешно удалена"
    context_object_name = 'task'
