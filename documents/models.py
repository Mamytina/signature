from django.db import models

from users.models import Users

# Create your models here.
class Document(models.Model):
   titre = models.CharField(max_length=200)
   fichier = models.FileField(upload_to='documents/')
   date_ajout = models.DateTimeField(auto_now_add=True)
   users = models.ForeignKey(Users, on_delete=models.CASCADE)