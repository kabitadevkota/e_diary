from django.db import models
from django.conf import settings


# Create your models here.
class Meetings(models.Model):
    title= models.CharField(max_length=100)
    date = models.DateField()
    time= models.DateTimeField(auto_now_add=True)
    venue= models.CharField(max_length=50)
    status = models.CharField(max_length=50)
