from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.forms import CreateUserForm
from django.contrib.messages.views import SuccessMessageMixin
from users.models import CustomUser
from task_manager.mixins import CustomLoginRequiredMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.values('id', 'first_name', 'last_name',
                                          'username', 'date_joined')[:15]
        return render(request, 'users/index.html', context={
            'users': users,
        })


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    model = CustomUser
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = "Пользователь добавлен"


class UserEditView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUserForm
    model = CustomUser
    template_name = 'users/update.html'
    success_message = "Пользователь изменен"
    success_url = reverse_lazy('users')


class UserDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = "Пользователь удален"