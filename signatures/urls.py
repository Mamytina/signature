
from django.contrib import admin
from django.urls import path
from users.views import *
from signatures.views import *

urlpatterns = [
    path('addSignature', addSignature,name='addSignature'),
    path('saveSignature/<int:users>', saveSignature,name='saveSignature'),
]
