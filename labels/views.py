from django.views.generic import ListView
from django.urls import reverse_lazy
from labels.models import Labels
from labels.forms import CreateLabelForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.mixins import CustomLoginRequiredMixin
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect


class IndexView(CustomLoginRequiredMixin, ListView):

    model = Labels
    template_name = 'labels/index.html'
    context_object_name = 'labels'


class CreateLabelView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateLabelForm
    model = Labels
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = "Метка добавлена"


class LabelEditView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateLabelForm
    model = Labels
    template_name = 'labels/update.html'
    success_message = "Метка изменена"
    success_url = reverse_lazy('labels')


class LabelDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = "Метка успешно удалена"
    context_object_name = 'label'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request, 'Невозможно удалить метку потому что она используется')
            return redirect(self.success_url)
