from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

def home(request):
    events = Events.objects.all()

    context = {
        'events': events
    }

    return render(request, 'backend/list.html', context)

# Create your views here.
