from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, UserSerializer, PermissionSerializer
from django.contrib.auth.models import User, Permission
from django.core import serializers
from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
import calendar

from .utils import Calendar
from .models import * 
from .forms import *

loginURL = reverse_lazy("backend:login")

def home(request):
    return render(request, 'backend/homepage.html')


@login_required(login_url= loginURL)
def events(request):
    if request.user.is_authenticated:
        user=request.user
        events = Events.objects.filter(user=user)
    

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(reverse('backend:events'))

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
            return redirect(reverse('backend: calendar'))

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
            return redirect(reverse('backend:calendar'))
    context = {
        
    }
    return render(request, 'backend/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect(reverse('backend:login'))

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

class CalendarView(generic.ListView):
    model = Events
    template_name = 'backend/calendar.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
