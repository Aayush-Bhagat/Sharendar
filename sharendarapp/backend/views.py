from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *
from django.contrib.auth.forms import UserCreationForm

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

def updateEvent(request, pk):
    event = Events.objects.get(id = pk)

    form = EventForm(instance= event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'backend/update.html', context)

def deleteEvent(request, pk):
    event = Events.objects.get(id = pk)

    if request.method == 'POST':
        event.delete()
        return redirect('/')

    context = {
        'event' : event
    }

    return render(request, 'backend/delete.html', context)

def registerUser(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'backend/register.html', context)

        




