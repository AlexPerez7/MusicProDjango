from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    color = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre