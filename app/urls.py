from django.db import router
from django.urls import path, include
from .views import home, contacto, galeria, agregar_producto, listar_productos, \
     modificar_producto, eliminar_producto, registro, ProductoViewSet, CategoriaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('categoria', CategoriaViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<int:id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
]