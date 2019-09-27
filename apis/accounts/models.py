from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Users(AbstractUser):
    address =models.CharField(max_length=80)
    user_picture= models.ImageField(upload_to='uploads')
    email = models.CharField(max_length=50,unique=True)
    
