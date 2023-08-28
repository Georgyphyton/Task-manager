from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = 'You are not logged in! Please log in.'
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class TaskOwnerMixin(UserPassesTestMixin):
    permission_denied_message = 'Задачу может удалить только ее автор'

    def test_func(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(reverse_lazy('tasks'))


class UserOwnerMixin(UserPassesTestMixin):
    permission_denied_message = 'У вас нет прав для изменения другого пользователя.'

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(reverse_lazy('users'))
