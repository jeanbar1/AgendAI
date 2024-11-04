from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }