from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Test


class AllTestsView(ListView):
    model = Test
    template_name = 'tests/all-tests.html'