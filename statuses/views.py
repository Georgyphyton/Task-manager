from django.views.generic import ListView
from django.urls import reverse_lazy
from statuses.models import Statuses
from statuses.forms import CreateStatusForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.mixins import CustomLoginRequiredMixin
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect


class IndexView(CustomLoginRequiredMixin, ListView):

    model = Statuses
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class CreateStatusView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateStatusForm
    model = Statuses
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = "статус добавлен"


class StatusEditView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateStatusForm
    model = Statuses
    template_name = 'statuses/update.html'
    success_message = "Статус изменен"
    success_url = reverse_lazy('statuses')


class StatusDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = "Статус успешно удален"
    context_object_name = 'status'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request, 'Невозможно удалить cстатус потому что он используется')
            return redirect(self.success_url)
