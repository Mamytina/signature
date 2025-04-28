from django.urls import path

from .views import UserListAPIView
from .views import signatureListAPIView
from .views import add_user
from .views import update_user
from .views import delete_user
from .views import add_signature,add_documnts
from .views import upload_signature


urlpatterns = [
    
    # Users
    path('api/users/', UserListAPIView.as_view(), name='user-list-api'),
    path('api/add-users/', add_user, name='add_user'),
    path('api/users_update/<str:user_id>/', update_user, name='update_user'),
    path('api/users_delete/<str:user_id>/', delete_user, name='delete_user'),
     
    # Signatures
    path('api/usersWithsignatures/', signatureListAPIView.as_view(), name='signature-list-api'),
    path('api/signature/', add_signature, name='add-signature'),
    path('api/upload-signature/<int:user_id>/', upload_signature, name='upload-signature'),
    
    
    # Document
    path('api/document/', add_documnts, name='add-signature'),
    
    
]
