from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, UserSerializer, PermissionSerializer
from django.contrib.auth.models import User, Permission

def home(request):
    return render(request, 'backend/homepage.html')


@login_required(login_url="login")
def events(request):
    if request.user.is_authenticated:
        user=request.user
        events = Events.objects.filter(user=user)
    

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
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'backend/register.html', context)

        
def loginUser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("events")
    context = {
        
    }
    return render(request, 'backend/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def profileUser(request):
    user=request.user
    events = Events.objects.filter(user=user)
    profile = userProfile.objects.get(user= user)

    context = {
        'events': events,
        'profile': profile,
        'user': user,
    }

    return render(request, 'backend/user.html', context)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

def calendar(request):
    return render(request, 'backend/calendar.html')