from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views import View

from .forms import UsuarioForm, UserForm
from .models import Usuario

class UsuarioCreate(View):
    def get(self, request):
        userform = UserForm()
        usuarioform = UsuarioForm()
        return render(request, 'usuario/usuario_create.html', {'userform': userform, 'usuarioform': usuarioform})
    
    
    def post(self, request):
        userform = UserForm(request.POST)
        usuarioform = UsuarioForm(request.POST)
        
        if userform.is_valid() and usuarioform.is_valid():
            User = UserForm.save(commit=False)
            User.set_password(usuarioform.cleaned_data['password'])
            User.save()
            Usuario - UsuarioForm.save(commit=False)
            Usuario.user = User
            Usuario.save()
            return redirect('login')
        return render(request, 'register.html', {'userForm': UserForm, 'usuarioForm': UsuarioForm})
    
@method_decorator(login_required, name='dispatch')
class Usuarioedit(View):
    def get(self, request):
        usuario = Usuario.objects.get(user=request.user)
        userform = UserForm(instance=request.user)
        usuarioform = UsuarioForm(instance=usuario)
        return render(request, 'usuario/usuarioedit.html', {'userform': userform, 'usuarioform': usuarioform})
    
    
    def post(self, request):
        usuario = Usuario.objects.get(user=request.user)
        userform = UserForm(request.POST, instance=request.user)
        usuarioform = UsuarioForm(request.POST, instance=usuario)
        
        if userform.is_valid() and usuarioform.is_valid():
            userform.save()
            usuarioform.save()
            return redirect('perfil')
        return render(request, 'usuario/usuarioedit.html', {'userform': userform, 'usuarioform': usuarioform})
    
    
    
@method_decorator(login_required, name='dispatch')
class Usuariodelete(View):
    def get(self,request ):
        return render(request, 'delete.html')
    
    
    def post(self, request):
        user = request.user
        user.delete()
        return redirect('home')
    
    
    
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    
    def post(self, request):
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
        
        
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')