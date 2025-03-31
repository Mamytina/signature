from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)   
    email = models.EmailField(unique=True)  
    role = models.CharField(max_length=50, default="users")        
    phone_number = models.CharField(max_length=15, unique=True)  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'numero']

  