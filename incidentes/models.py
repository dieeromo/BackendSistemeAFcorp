from django.db import models
from users.models import User


############ PARA INCIDENTES
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


###### PARA BITACORA DE EQUIPOS

class Equipos_red(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    fecha_instalacion = models.DateField()
    nodo_inicial = models.ForeignKey(Nodo, on_delete=models.CASCADE, related_name='nodo_inicial')
    nodo_actual = models.ForeignKey(Nodo, on_delete=models.CASCADE, related_name='nodo_actual')
    activo = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    alias = models.TextField(null=True, blank=True)

class Mantenimientos_equipos(models.Model):
    equipo = models.ForeignKey(Equipos_red, on_delete=models.CASCADE)
    fecha = models.DateField()
    problema = models.TextField()
    solucion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Movimientos_equipos(models.Model):
    equipo = models.ForeignKey(Equipos_red, on_delete=models.CASCADE)
    fecha = models.DateField()
    nodo_salida = models.ForeignKey(Nodo, on_delete=models.CASCADE, related_name='nodo_salida')
    nodo_llegada = models.ForeignKey(Nodo, on_delete=models.CASCADE, related_name='nodo_llegada')
    observacion = models.TextField(null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


######  PARA BITACORA DE TRABAJOS DE FIBRA
class Tipo_fibra(models.Model):
    tipo = models.CharField(max_length=60)
    numero_hilos = models.IntegerField()
    descripcion = models.TextField()
    marca = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Trazado_FO(models.Model):
    identificador = models.TextField()
    nombre = models.TextField()
    descripcion = models.TextField(null=True, blank=True)
    tipo_fibra = models.ForeignKey( Tipo_fibra, on_delete=models.CASCADE)
    fecha = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tipo_trabajo(models.Model):
    tipo_trabajo = models.TextField()

class Trabajos_FO(models.Model):
    trazado = models.ForeignKey( Trazado_FO, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_trabajo = models.ForeignKey( Tipo_trabajo, on_delete=models.CASCADE)
    tipo_fibra_cambio = models.ForeignKey( Tipo_fibra, on_delete=models.CASCADE)
    descripcion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    
