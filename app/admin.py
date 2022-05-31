from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "marca", "precio", "disponibilidad", "stock", "categoria"]
    list_editable = ["precio", "disponibilidad", "stock"]
    search_fields = ["nombre", "categoria__nombre"]
    list_filter = ["categoria", "disponibilidad"]
    list_per_page = 10

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)