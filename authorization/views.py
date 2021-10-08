from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .forms import RegistrationForm

from django.views.generic import CreateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'base.html')

class RegisterUserForm(SuccessMessageMixin, CreateView):
    model = User
    template_name = ''
    form_class = RegistrationForm
    success_url = ''
    success_message = 'Successfully created!'

