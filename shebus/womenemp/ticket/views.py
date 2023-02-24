from django.shortcuts import render
# from ticket.models import Ticket
from django.db import connection, IntegrityError
from django.contrib import messages
from accounts.models import User
from django.shortcuts import redirect

# Create your views here.
def ticket_book(request,*args):
    '''context = {}
    slot = request.POST['slot']
    date = request.POST['date']
    women_id = request.POST['women']
    women = User.objects.get(pk=women_id)
    
    try:
        ticket = Ticket.objects.create(
            women=women,
            date = date,
            slot = slot,
            status=False,
        )
    except IntegrityError:
        messages.add_message(request, messages.ERROR, f'Already booked ticket on {date}!')'''
    return redirect('index.html')

