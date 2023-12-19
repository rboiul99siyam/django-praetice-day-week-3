from django.urls import path,include

from . import views
urlpatterns = [
  path('register/', views.register,name='res'),
  path('login/', views.Login.as_view(),name='login'),
  path('logout/', views.logout.as_view(),name='logout'),
]
