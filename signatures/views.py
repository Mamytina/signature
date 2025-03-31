import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import Signatures
from django.contrib.auth.decorators import login_required
from users.models import Users

# Create your views here.

def addSignature(request):
    if request.method=='POST':
         signature_data = request.POST.get('signature')
          # Convertir l'image de la signature en fichier
         format, imgstr = signature_data.split(';base64,')  # Extraire le format de l'image et les données
         ext = format.split('/')[1]  # Extraire l'extension du type d'image (png, jpeg, etc.)
         image_data = base64.b64decode(imgstr)  # Décoder les données en base64

         # Créer un fichier temporaire
         file_name = f"signature_{request.user.id}.{ext}"
         file = ContentFile(image_data, name=file_name)
         
          # Sauvegarder la signature dans la base de données
         test=Users.objects.get(pk=1)
         Signatures.objects.create(user=test,signature_image=file)
         print('vita')
    return render (request,'createSignature.html')

def saveSignature(request,id_users):
    if request.method=='POST':
         signature_data = request.POST.get('signature')
          # Convertir l'image de la signature en fichier
         format, imgstr = signature_data.split(';base64,')  # Extraire le format de l'image et les données
         ext = format.split('/')[1]  # Extraire l'extension du type d'image (png, jpeg, etc.)
         image_data = base64.b64decode(imgstr)  # Décoder les données en base64

         # Créer un fichier temporaire
         file_name = f"signature_{request.user.id}.{ext}"
         file = ContentFile(image_data, name=file_name)
         
          # Sauvegarder la signature dans la base de données
         users=Users.objects.get(pk=id_users)
         Signatures.objects.create(user=users,signature_image=file)
         print('vita')
    return render (request,'createSignature.html',{'id_users':id_users})
          
