from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .forms import RegistrationForm

from django.views.generic import CreateView, FormView, ListView, DetailView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


user = get_user_model()

# ! don`t forget template
def index(request):
    return render(request, '.html')


class AllPostsList(ListView):
    model = Post
    template_name = ''
    paginated_by = 20

    def get_context_data(self):
        context = Post.objects.all() # order_by + moderated
        return context

# ! Есть страница поста

class PostDetail(DetailView, pk):
    model = Post
    # later


# Есть страница с списком постов пользователя

class AllUsersList(ListView):
    model = User
    template_name = ''

    def get_queryset(self):
        return User.objects.all()


# !  Есть страница профиля публичная

class RegisterUserForm(SeccessMessageMixin, FormView):
    template_name = ''
    form_class = RegistrationForm
    success_url = ''
    success_message = 'Successfully created!'

    # ! add validation
    # def form_valid(self, form):
        #

class UpdateUserProfile(LoginRequiredMixin, FormView):
    template_name = ''
    form_class = RegistrationForm
    success_url = ''
    success_message = 'Successfully updated!'

    # ! validation form

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['label', 'short_description', 'image', 'full_description']
    template_name = ''
    success_url = ''
