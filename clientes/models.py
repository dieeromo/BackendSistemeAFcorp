from django.db import models
from users.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=15)
    telefono2 = models.CharField(max_length=15,blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    observacion = models.TextField(blank=True, null=True)

