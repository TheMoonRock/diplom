from .forms import UserLoginForm
from django.urls import path, include
from .views import UserLoginView

from . import views

app_name = 'techsupport'

urlpatterns = [
    path('', views.warning_list),
    path('create/', views.create_problem, name='create_problem'),
    path('profile/', views.profile_view, name="profile"),
    path('user_problems/', views.user_problems, name='user_problems'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]
