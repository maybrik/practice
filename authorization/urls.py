from django.contrib.auth import views as auth_views

from django.urls import path, include

from .views import RegisterUserForm, UserUpdate


urlpatterns = [
    path('register/', RegisterUserForm.as_view(), name='register'),
    path('profile/edit/', UserUpdate.as_view(), name='user_update'),
    path('accounts/', include('django.contrib.auth.urls')),
]
]
