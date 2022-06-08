from .models import Producto, Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source='categoria.nombre')
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria')
    nombre = serializers.CharField(required=True, max_length=50, min_length=3)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre_iexact=value).exists()

        if existe:
            raise serializers.ValidationError("El nombre del producto ya existe")
        
        return value

    class Meta:
        model = Producto
        fields = '__all__'