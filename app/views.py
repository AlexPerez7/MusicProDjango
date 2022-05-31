from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')