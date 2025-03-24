from django.db import models

# Create your models here.
class superAdmin(models.Model):
    name = models.CharField(max_length=100)  
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.name