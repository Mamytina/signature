from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import Users
from signatures.models import Signatures
from rest_framework import status
from .serializers import UserSerializer,SignatureSerializer,DocumentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import base64
import uuid
from django.core.files.base import ContentFile
from django.http import JsonResponse


# Users

class UserListAPIView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_user(request, user_id):
    try:
        user = Users.objects.get(id=user_id)  # Récupère l'utilisateur à partir de son ID
    except Users.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()  # Enregistre les données mises à jour
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = Users.objects.get(id=user_id)  # Récupère l'utilisateur à partir de son ID
        user.delete()
    except Users.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response( status=status.HTTP_400_BAD_REQUEST)



# Signature

class signatureListAPIView(APIView):
    def get(self, request):
        signatures = Signatures.objects.all()
        serializer = SignatureSerializer(signatures, many=True)
        return Response(serializer.data)
    

def add_signature(request):
    serializer = SignatureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload_signature(request,user_id):
    signature_data = request.FILES.get('signature')

    user = Users.objects.get(id=user_id)
     # créer et enregistrer la signature
    signature = Signatures.objects.create(user=user, signature_image=signature_data)

    return JsonResponse({'message': 'Signature enregistrée avec succès', 'signature_url': signature.signature_image.url})

        
        
# Documnt

@api_view(['POST'])
def add_documnts(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)