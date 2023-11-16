
from django.db import models
from users.models import User

class Empresa_corp(models.Model):
    empresa = models.CharField(max_length=100)

class Caja_empresa(models.Model):
    caja = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

class Modo_CompraVenta(models.Model):
    modo_cv = models.CharField(max_length=100)  #contado/credito

class Bodega(models.Model):
    bodega = models.CharField(max_length=100)  #contado/credito

