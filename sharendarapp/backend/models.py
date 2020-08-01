from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 100)
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length = 300, blank=True)
    
    def __str__(self):
        return self.title


