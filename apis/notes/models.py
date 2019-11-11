from django.db import models
from django.conf import settings


# Create your models here.
class Notes(models.Model):
    title= models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    description= models.TextField()
    status = models.CharField(max_length=50)
    