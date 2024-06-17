from .forms import UserLoginForm
from django.urls import path, include
from .views import UserLoginView

from . import views

app_name = 'techsupport'

urlpatterns = [
    path('', views.UserLoginView.as_view(), name='user_login'),
    path('create/', views.create_problem, name='create_problem'),
    path('profile/', views.profile_view, name="profile"),
    path('user_problem/', views.user_problem, name='user_problem'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]
