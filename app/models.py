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
    imagen = models.ImageField(upload_to='productos/', blank=True)


    def __str__(self):
        return self.nombre

#class ImagenProducto (models.Model):
#    imagen = models.ImageField(upload_to='productos')
#    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')


#Arrelgos con los tipos de consultas
opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
]

class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre