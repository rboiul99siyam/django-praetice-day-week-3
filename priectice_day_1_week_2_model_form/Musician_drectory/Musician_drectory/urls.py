from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('user_athunticated/', include('user_auth.urls')),
    path('', views.home, name='homePage')

]
