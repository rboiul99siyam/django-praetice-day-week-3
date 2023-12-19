from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.Register,name='register'),
    path('user_login/', views.user_login,name='login'),
    path('user_logout/', views.user_logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('change_pass/', views.chanage_pass,name='pass1'),
    path('change_pass2/', views.chanage_pass2,name='pass2'),
]
