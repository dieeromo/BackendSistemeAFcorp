from django.contrib import admin
from . models import Nivel, Red, Nodo, TipoIncidente, Incidente, Equipos_red, Mantenimientos_equipos, Movimientos_equipos
from . models import Tipo_fibra,Trabajos_FO,Tipo_trabajo,Trazado_FO
# Register your models here.
admin.site.register(Nivel)
admin.site.register(Red)
admin.site.register(Nodo)
admin.site.register(TipoIncidente)
admin.site.register(Incidente)

#Tablas de datos de bitacora equipos
admin.site.register(Equipos_red)
admin.site.register(Mantenimientos_equipos)
admin.site.register(Movimientos_equipos)

#Tablas para bitacora Fibra optica
admin.site.register(Tipo_fibra)
admin.site.register(Trabajos_FO)
admin.site.register(Tipo_trabajo)
admin.site.register(Trazado_FO)


