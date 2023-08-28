from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = _('You are not logged in! Please log in.')
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class TaskOwnerMixin(UserPassesTestMixin):
    permission_denied_message = _('A task can only be deleted by its author')

    def test_func(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(reverse_lazy('tasks'))


class UserOwnerMixin(UserPassesTestMixin):
    permission_denied_message = _("You don't have the rights to change another user.")

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(reverse_lazy('users'))
