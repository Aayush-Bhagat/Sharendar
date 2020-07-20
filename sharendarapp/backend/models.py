from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length = 100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length = 300)
    def __str__(self):
        return self.title
