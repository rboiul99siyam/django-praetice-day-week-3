from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm,SetPasswordForm
from . forms import CreationForm
from django.contrib import messages

def Register(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Create Successfully !')
            form.save()
            return redirect('register')
    else:
        form = CreationForm()
    return render(request,'register.html',{'form':form,'type':'Register'})

def user_logout(request):
    messages.success(request,'Logged out Successfully ')
    logout(request)
    return redirect('login')

def user_login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    messages.success(request,'Login succeessfully !')
                    login(request, user)
                    return redirect('profile')
        else:
             form = AuthenticationForm()
        return render(request,'register.html',{'form':form,'type':'Login'})
    
def profile(request):
    return render(request,'profile.html')

def chanage_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                messages.success(request,'Already password change Successfully !')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')

        else:
            form = PasswordChangeForm(user = request.user)
        return render(request,'changepass.html',{'form':form,'type':'Chanage Password '})
    else:
        return redirect('login')


def chanage_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                messages.success(request,'Already password change Successfully !')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')

        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'changepass.html',{'form':form,'type':'Chanage Password'})
    else:
        return redirect('login')