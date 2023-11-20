from django.db import models
from users.models import User

# Create your models here.

class Nivel(models.Model):
    nivel = models.CharField(max_length=60)

class Red(models.Model):
    red = models.CharField(max_length=60)

class Nodo(models.Model):
    nodo = models.CharField(max_length=60)

class TipoIncidente(models.Model):
    tipo = models.CharField(max_length=60)

class Incidente(models.Model):
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    red = models.ForeignKey(Red, on_delete=models.CASCADE)
    nodo = models.ForeignKey(Nodo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoIncidente, on_delete=models.CASCADE)
    afectados = models.IntegerField()
    descripcion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   


