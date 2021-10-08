from django.shortcuts import render, reverse, redirect

from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .forms import Feedback

from django.views.generic import CreateView, FormView, DetailView, UpdateView, ListView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


user = get_user_model()


def index(request):
    return render(request, 'homepage.html')


class AllPostsList(ListView):
    model = Post
    template_name = 'posts_list.html'
    queryset = Post.objects.filter(is_published=True)
    paginate_by = 20


class PostDetail(DetailView, pk_url_kwarg):
    model = Post
    template_name = 'post_detailed.html'
    pk_url_kwarg = 'id'


class AllUsersList(ListView):
    model = User
    template_name = 'users_list.html'
    queryset = User.objects.all()
    paginate_by = 20


def get_user_profile(request, username):
    user = User.objects.get(username=username, is_staff=False)
    # alternative: user = get_object_or_404(user, pk=pk, is_staff=False)
    posts = Post.objects.filter(user=username).filter(is_published=True)
    context = {'object': user}
    return render(request, 'blog/user_detailed.html', context)


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['label', 'short_description', 'image', 'full_description', 'user', 'is_published']
    template_name = 'post_create.html'

    def get_success_url(self):
        send_mail('Новый пост', f"{self.object.label}", "admin@admin.com", ['admin@admin.com'])
        return reverse('blog:post_detailed', kwr={'pk': self.object.pk})


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    fields = ['label', 'short_description', 'image', 'full_description', 'user', 'is_published']
    template_name = 'post_update.html'

    def get_context_data(self, *args, **kwargs):
        queryset = Post.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data()
        context['posts_list'] = queryset
        return context

    def get_success_url(self):
        send_mail('Пост был обновлён:', f"{self.object.label}", "admin@admin.com", ['admin@admin.com'])
        return reverse('blog:post_detailed', kwr={'pk': self.object.pk})


class PostUserListView(generic.ListView):
    model = Post
    template_name = 'post_user_list.html'

    def get_context_data(self, *args, **kwargs):
        queryset = Post.objects.get(author_id=self.kwargs['pk']).order_by('pk')
        context = super().get_context_data()
        context['posts_list'] = queryset
        return context


def feedback_form(request):
    if reques.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            email = form.cleaned_data('email')
            feedback_message = form.cleaned_data('feedback_message')
            send_mail(email, feedback_message, [admin@admin.com])
            return redirect('homepage')
        else:
            form = Feedback()
            return render(request, 'feedback.html', context={"form": form})
