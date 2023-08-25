from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = 'You are not logged in! Please log in.'
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()
