from django.urls import path
from . import views

app_name = 'equipment_manager'

urlpatterns = [
    path('computers/', views.computer_list, name='computer_list'),
    path('computers/add/', views.add_computer, name='add_computer'),
]
