from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = _("You are logged in")

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out'))
    return redirect('main')
