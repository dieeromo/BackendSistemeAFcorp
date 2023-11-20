from django.db import models
from users.models import User

# Create your models here.

class Tipo_producto(models.Model):
    tipo = models.CharField(max_length=60)

class Subtipo_producto(models.Model):
    subtipo = models.CharField(max_length=60)

class Estado_producto(models.Model):
    estado = models.CharField(max_length=30)

class Producto(models.Model):
    modelo = models.TextField()
    descripcion = models.TextField()
    codigo = models.CharField(max_length=30)

    tipo = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    subtipo = models.ForeignKey(Subtipo_producto, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado_producto, on_delete=models.CASCADE)

    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    precio_salida = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    precio_promo = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    
    seguimiento = models.BooleanField(default=True)
    observacion = models.TextField(null=True, blank= True)
    fecha_modificacion = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PrecioProductosIn(models.Model):
    producto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    fecha_modificacion = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PrecioProductosOut(models.Model):
    producto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    fecha_modificacion = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
   



    