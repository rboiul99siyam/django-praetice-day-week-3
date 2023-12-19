from django.shortcuts import render
from album.models import Album_form
def home(res):
    data = Album_form.objects.all() 
    return render(res,'home.html',{'data':data} )