from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
    class Meta:
        model= Events
        fields = '__all__'

