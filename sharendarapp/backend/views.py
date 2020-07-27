from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *

def home(request):
    events = Events.objects.all()

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'events': events,
        'form': form
    }

    return render(request, 'backend/list.html', context)


