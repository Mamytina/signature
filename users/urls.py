
from django.contrib import admin
from django.urls import path
from users.views import *

urlpatterns = [
    path('viewsUsers', viewsUsers,name='viewsUsers'),
    path('searchIdUsers/<int:id_users>',searchIdUsers,name='searchIdUsers'),
    path('deleteUsers/<int:id_users>',deleteUsers,name='deleteUsers'),
    path('addUsers', addUsers,name='addUsers'),
    path('editeUsers', editeUsers,name='editeUsers'),
    path('home',home,name='home'),
    path('loginUsers',loginUsers,name='loginUsers'),
]
