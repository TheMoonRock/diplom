from django.shortcuts import render
from django.http import HttpResponse
from .models import problems, status_storage
from django import forms

# Create your views here.

class status_storage_form(forms.ModelForm):
    class some_base:
        model = problems
        fields = ['status_storage']

def warning_list(request):
    if request.method == 'POST':
        form = status_storage_form(request.POST)
        if form.is_valid():
            form.save()
            # Выполните другие действия после сохранения формы
    else:
        form = status_storage_form()
    
    context = {
        'form': form,
    }
    return render(request, context)
