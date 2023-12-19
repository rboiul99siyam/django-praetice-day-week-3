from django.shortcuts import render, redirect

# Create your views here.
from . import forms
from . import models


def Album(res):
    if res.method == 'POST':
        form = forms.AlbumModelForm(res.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    else:
        form = forms.AlbumModelForm()
    return render(res,'album.html',{'form': form})

def edit_post(request, id):
    post = models.Album_form.objects.get(pk=id)
    form = forms.AlbumModelForm(instance=post)
    if request.method == "POST":
        form = forms.AlbumModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("homePage")

    return render(request, "album.html", {"form": form})

def DeletePost(res,id):
    post = models.Album_form.objects.get(pk=id)
    post.delete()
    return redirect('homePage')

