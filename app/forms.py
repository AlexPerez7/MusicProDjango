from django import forms

from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ['nombre', 'email', 'tipo_consulta', 'mensaje', 'avisos',]
        fields = '__all__' #todos los campos(lo mismo que arriba)

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'