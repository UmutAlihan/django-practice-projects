from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# The reason is that for all generic class-based views the urls are not loaded when the file is imported,
# so we have to use the lazy form of reverse to load them later when they're available
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
