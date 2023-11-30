from django.contrib import admin
from . models import Nivel, Red, Nodo, TipoIncidente, Incidente, Equipos_red, Mantenimientos_equipos, Movimientos_equipos

# Register your models here.
admin.site.register(Nivel)
admin.site.register(Red)
admin.site.register(Nodo)
admin.site.register(TipoIncidente)
admin.site.register(Incidente)

#Bases de datos de bitacora equipos
admin.site.register(Equipos_red)
admin.site.register(Mantenimientos_equipos)
admin.site.register(Movimientos_equipos)


