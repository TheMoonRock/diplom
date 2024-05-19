from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Problems
from django import forms

# Create your views here.

class ProblemsForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ['id_request', 'nemployee', 'request_from_date', 'name_of_problem', 'description_of_problem']

def warning_list(request):
    all_problems = Problems.objects.all()

    return HttpResponse(all_problems)

def create_problem(request):
    if request.method == 'POST':
        form = ProblemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_problem')  # Замените на нужный URL-адрес после успешного сохранения
    else:
        form = ProblemsForm()
    
    return render(request, 'create_problem.html', {'form': form})


