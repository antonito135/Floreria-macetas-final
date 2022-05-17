from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *

# Creamos un template del formulario


class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=4,max_length=25)
    precio = forms.IntegerField(min_value=400)
    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','tipo','imagen']
        


class SuscripcionForm(ModelForm):
    class Meta:
        model = Suscripcion
        fields=['suscrito','email']

class UsuarioForm(ModelForm):
    nombre = forms.CharField(min_length=4,max_length=20)
    class Meta:
        model = Usuario
        fields = ['codigo','nombre','apellido','email','password','tipo_usuario']
     

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['nombre','precio','imagen']