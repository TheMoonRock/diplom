from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.warning_list, name='tech_support'),
    path('create/', views.create_problem, name='create_problem'),
    path('profile', views.profile, name="profile"),
]
