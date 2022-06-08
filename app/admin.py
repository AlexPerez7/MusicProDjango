from django.contrib import admin
from .models import Categoria, Producto, Contacto, ImagenProducto
from .forms import ProductoForm, ContactoForm

# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "marca", "precio", "disponibilidad", "stock", "categoria"]
    list_editable = ["precio", "disponibilidad", "stock"]
    search_fields = ["nombre", "categoria__nombre"]
    list_filter = ["categoria", "disponibilidad"]
    list_per_page = 10
    form = ProductoForm
    inlines = [ImagenProductoAdmin]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_per_page = 10

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)