from django.shortcuts import render, redirect
from .models import Computer
from .forms import ComputerForm

def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'computer_list.html', {'computers': computers})

def add_computer(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_manager:computer_list')
    else:
        form = ComputerForm()
    return render(request, 'add_computer.html', {'form': form})
