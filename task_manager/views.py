from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = "Вы вошли в систему"

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('main')
