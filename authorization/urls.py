from django.contrib.auth import views as auth_views

from django.urls import path

from .views import RegisterUserForm


urlpatterns = [
    path('register/', RegisterUserForm.as_view(), name='register'),
]
