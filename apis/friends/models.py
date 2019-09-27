from django.db import models
from django.conf import settings
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Friends(models.Model):
    first_name = models.CharField(max_length=25,default='DEFAULT VALUE')
    last_name = models.CharField(max_length=25,default='DEFAULT VALUE')
    GENDER=(("0","male"),("1","Female"),("2","others"))
    address =models.CharField(max_length=80)
    email = models.CharField(max_length=50,unique=True,blank=True)
    cover_image = models.ImageField(upload_to='uploads')
    date_of_birth = models.DateTimeField(auto_now_add=True)
    phone_no = models.CharField(max_length=10)
    gender= models.CharField(choices=GENDER,max_length=1)
    created_by= models.CharField(max_length=15)
    created_at= models.DateTimeField(auto_now_add=True)
    

    
  


