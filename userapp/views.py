from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userapp.forms import UserLoginForm, UserCreationCustomForms


# Create your views here.


class LoginUserView(LoginView):
    template_name = 'registration/login.html'
    form_class = UserLoginForm


class LogoutUserView(LogoutView):
    pass


class CreateUserView(CreateView):
    model = get_user_model()
    form_class = UserCreationCustomForms
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        valid = super(CreateUserView, self).form_valid(form)
        username, password = form.cleaned_data['username'], form.cleaned_data['password1']
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class PasswordResetUserView(PasswordResetView):
    template_name = ''