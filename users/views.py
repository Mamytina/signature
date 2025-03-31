from django.shortcuts import render,redirect
from users.models import Users
from signatures.models import Signatures
import base64
from django.core.files.base import ContentFile
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def viewsUsers(request):
    data=Users.objects.all()
    return render(request,'viewsUsers.html',{'data':data})
    

def addUsers(request):
    if request.method == "POST":
        last_name= request.POST.get("nom")
        first_name= request.POST.get("prenom")
        email= request.POST.get("email")
        phone_number= request.POST.get("nom")
        signature_data = request.POST.get('signature')
        
        
        # Convertir l'image de la signature en fichier
        format, imgstr = signature_data.split(';base64,')  # Extraire le format de l'image et les données
        ext = format.split('/')[1]  # Extraire l'extension du type d'image (png, jpeg, etc.)
        image_data = base64.b64decode(imgstr)  # Décoder les données en base64

        # Créer un fichier temporaire
        file_name = f"signature_{request.user.id}.{ext}"
        file = ContentFile(image_data, name=file_name)
        
        # Sauvegarder l'utilisateurs dans la base de données
        Users.objects.create( first_name=first_name,last_name=last_name,email=email,phone_number=phone_number)
        
        # Sauvegarder la signature dans la base de données
        id_users=Users.objects.filter(email=email)[0].pk
        users=Users.objects.get(pk=id_users)
        Signatures.objects.create(user=users,signature_image=file)

        print('ajouter')
        
        return redirect('index')
    return render(request,'addUsers.html')


def searchIdUsers(request,id_users):
    data=Users.objects.get(pk=id_users)
    return render(request,'editeUsers.html',{'data':data})

def editeUsers(request):
    if request.method=='POST':
         last_name= request.POST.get("nom")
         first_name= request.POST.get("prenom")
         email= request.POST.get("email")
         phone_number= request.POST.get("nom")
         id_users=request.POST.get("id_users")
         users=Users.objects.get(pk=id_users)
         if request.method=='POST':
            users.first_name=first_name
            users.last_name=last_name
            users.email=email
            users.phone_number=phone_number
            users.save()         
            
            return redirect('viewsUsers')
    return render(request,'editeUsers.html')



def deleteUsers(request,id_users):
    data=Users.objects.get(pk=id_users)
    data.delete()
    return redirect('viewsUsers')
    # return render(request,'viewsUsers.html')
    
    
    
def loginUsers(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')

        # Vérification des accès admin
        if email == 'admin@gmail.com' and name == 'admin':
            return redirect('home')

        # Recherche de l'utilisateur
        user = Users.objects.filter(email=email, first_name=name).first()

        if user:  # Vérifie si l'utilisateur existe
            request.session['id_users'] = user.pk
            request.session['first_name_users'] = user.first_name
            request.session['last_name_users'] = user.last_name
            request.session['email_users'] = user.email  # Correction du nom de clé

            return redirect('viewsUsers')

        # Si l'utilisateur n'est pas trouvé, on reste sur la page de connexion
        return render(request, 'index.html', {'error': 'Utilisateur non trouvé'})