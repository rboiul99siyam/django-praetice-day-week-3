from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('Add_Musician/' , views.music, name='Add_Musician')
]
