from django.db import models
from users.models import Users
# Create your models here.
class Signatures(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    signature_image = models.ImageField(upload_to="signatures/")  # Stockage l’image de la signature
    created_at = models.DateTimeField(auto_now_add=True)