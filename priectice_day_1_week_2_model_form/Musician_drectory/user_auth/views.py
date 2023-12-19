from django.shortcuts import render,redirect
from user_auth.forms import registerForm
# Create your views here.
from django.contrib.auth.views import LoginView ,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('res')
    else:
        form = registerForm()
    return render(request,'res.html',{'form':form,'type':'Register'})


class Login(LoginView):
    template_name = 'res.html'
    def get_success_url(self) -> str:
        return reverse_lazy('Add_Musician')
    def form_valid(self,form):
        messages.success(self.request,'Login Successfully ')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.warning(self.request,'Login data Incorect')
        return super().form_invalid(form)
    
    def get_context_data(self,**Kwargs):
        context = super().get_context_data(**Kwargs)
        context['type'] = 'Login'
        return context


class logout(LogoutView):
    def get_success_url(self)->str:
        return reverse_lazy('homePage')

    
    
