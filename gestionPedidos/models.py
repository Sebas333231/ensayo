from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombreCliente = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    email = models.EmailField(blank=True, null= True)
    telefono = models.CharField(max_length = 10)

    def __str__(self):

        return 'Nombre: ' + self.nombreCliente + ' Telefono: ' + self.telefono
    
class Articulos(models.Model):
    
    nombre = models.CharField(max_length = 30, verbose_name="NombreArticulo")#Sirve para relacionar tablas
    seccion = models.CharField(max_length = 30)
    precio = models.IntegerField()


    def __str__(self):
        nombre = self.nombre
        seccion = self.seccion
        precio = self.precio
        return 'Nombre ' + nombre + ', Seccion ' + seccion + ', precio ' + str(precio)


class Pedidos(models.Model):

    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()