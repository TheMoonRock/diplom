from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Problems
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserLoginForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'user_login.html'  # Создайте шаблон user_login.html для отображения формы аутентификации
    form_class = UserLoginForm
    success_url = reverse_lazy('user_problems')  # После успешной аутентификации перенаправить на страницу user_problems

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
            return redirect(reverse_lazy('techsupport:profile'))  # Замените на нужный URL-адрес после успешного сохранения
    else:
        form = ProblemsForm()
    
    return render(request, 'create_problem.html', {'form': form})

def profile_view(request):
    return render(request, 'authreg/profile.html')

@login_required
def user_problems(request):
    user_problems = Problems.objects.filter(user=request.user)
    return render(request, 'user_problems.html', {'user_problems': user_problems})
