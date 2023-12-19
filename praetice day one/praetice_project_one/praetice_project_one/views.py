from django.shortcuts import render

def home(res):
    return render(res,'home.html')