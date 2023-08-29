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
from django.utils.translation import gettext_lazy as _


class IndexView(CustomLoginRequiredMixin, ListView):

    model = Statuses
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class CreateStatusView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateStatusForm
    model = Statuses
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status successfully created")


class StatusEditView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateStatusForm
    model = Statuses
    template_name = 'statuses/update.html'
    success_message = _("Status successfully changed")
    success_url = reverse_lazy('statuses')


class StatusDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _("Status successfully deleted")
    context_object_name = 'status'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request, _("It is not possible to delete the status because it is being used"))
            return redirect(self.success_url)
