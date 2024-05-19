from django.contrib import admin

# Register your models here.

from .models import Problems, Employee

admin.site.register(Problems)
admin.site.register(Employee)
