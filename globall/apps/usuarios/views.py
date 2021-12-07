
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class UserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password1', "password2")

class SignUpView(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/signup.html'