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
from django.utils.translation import gettext_lazy as _


class IndexView(CustomLoginRequiredMixin, ListView):

    model = Labels
    template_name = 'labels/index.html'
    context_object_name = 'labels'


class CreateLabelView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateLabelForm
    model = Labels
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _("The label was created successfully")


class LabelEditView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateLabelForm
    model = Labels
    template_name = 'labels/update.html'
    success_message = _("Label changed successfully")
    success_url = reverse_lazy('labels')


class LabelDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _("The label was successfully deleted")
    context_object_name = 'label'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request,
                           _('It is not possible to delete the label because it is being used'))
            return redirect(self.success_url)
