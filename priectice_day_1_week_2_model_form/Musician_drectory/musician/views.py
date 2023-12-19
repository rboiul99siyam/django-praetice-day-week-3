from django.shortcuts import render,redirect

# Create your views here.
from . import forms
def music(res):
    if res.method == 'POST':
        form = forms.Musician_form(res.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('Add_Musician')
    else:
        form = forms.Musician_form()
        return render(res,'music.html',{'form':form})