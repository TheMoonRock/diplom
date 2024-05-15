from django.shortcuts import render, redirect
from .models import Ticket
from django.contrib.auth.decorators import login_required

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets/list.html', {'tickets': tickets})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ticket = Ticket.objects.create(title=title, description=description, user=request.user)
        return redirect('ticket_list')
    return render(request, 'tickets/create.html')

@login_required
def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'tickets/detail.html', {'ticket': ticket})

