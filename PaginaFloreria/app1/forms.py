from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):

    class Meta:
        model= Producto
        fields = ['nombre','precio','stock','descripcion','categoria', 'imagen']

class CustomUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']