from email.mime import image
from django import forms

from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ['nombre', 'email', 'tipo_consulta', 'mensaje', 'avisos',]
        fields = '__all__' #todos los campos(lo mismo que arriba)

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, min_length=3) #definie un maximo y un minimo de caracteres
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=5)]) #no es obligatorio ponerlo en el formulario
    precio = forms.IntegerField(min_value=0) #valor minimo de 0

    def clean_nombre(self): #metodo para validar la existencia del nombre
        nombre = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre=nombre).exists()
        if existe:
            raise forms.ValidationError("El nombre ya existe")
        return nombre
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']