from django.urls import path

from . import views

urlpatterns = [
    path('', views.warning_list, name='tech_support'),
]
