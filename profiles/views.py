from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView

from .models import Profile

from .form import SingUpForm

# Create your views here.
class SingUpView(CreateView):
    model = Profile
    form_class = SingUpForm

    def form_class(self, form):