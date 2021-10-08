from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login

from .forms import RegistrationForm

from django.views.generic import CreateView, DetailView, UpdateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'homepage.html')


class RegisterUserForm(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = 'homepage.html'
    success_message = 'Successfully created!'

    def form_valid(self, form):
        user = form.save()

        username = self.request.POST['username']
        password = self.request.POST['password']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterUserForm, self).valid(form)


class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User
    fields = ['firstname', 'lastname', 'email']
    template_name = 'user_update.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_profile.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserPublicProfileView(DetailView):
    model = User
    template_name = 'user_public_profile.html'
