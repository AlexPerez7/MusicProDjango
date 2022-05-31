from django import forms

from .models import Contacto

class ContactoForm(forms.Form):

    class Meta:
        model = Contacto
        #fields = [
        #    'nombre',
        #    'email',
        #    'tipo_consulta',
        #    'mensaje',
        #    'avisos',
        #]
        fields = '__all__' #todos los campos(lo mismo que arriba)