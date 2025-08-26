from django.db import models
from django.utils import timezone
# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=30,default="unknown")
    temperature = models.CharField(max_length=50)
    wind = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.city} - {self.temperature} - {self.description}"
