from django.contrib.auth import views as auth_views

from django.urls import path

from .views import AllPostsList, PostDetail, PostCreateView, PostUpdateView, AllUsersList, PostUserListView
from .views import get_user_profile, feedback_form


urlpatterns = [
    path('posts/', AllPostsList.as_view(), name='posts'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detailed'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/update/<int:pk', views.PostUpdateView(), name='post_update'),
    path('accounts/', AllUsersList.as_view(), name='users'),
    path('accounts/<int:username>', views.get_user_profile, name='user_detailed'),
    path('posts/<int:username>', views.PostUserListView.as_view(), name='post_user_list'),
    path('help/', views.feedback_form, name='feedback'),
]
