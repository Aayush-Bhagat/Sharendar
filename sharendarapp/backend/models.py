from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 100)
    start_time = models.DateTimeField( default = timezone.now)
    end_time = models.DateTimeField( default= timezone.now)
    description = models.CharField(max_length = 300, blank=True)
    
    def __str__(self):
        return self.title


class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 300, blank=True)
    contact1 = models.TextField(max_length = 100, blank=True)
    contact2 = models.TextField(max_length = 100, blank=True)
    contact3 = models.TextField(max_length = 100, blank=True)
    contact4 = models.TextField(max_length = 100, blank=True)

    def __str__(self):
        return self.bio


