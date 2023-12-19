from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('Add_Album/' , views.Album, name='Add_Album'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('DeletePost/<int:id>', views.DeletePost, name='delete'),
]
