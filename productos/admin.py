from django.contrib import admin
from . models import Tipo_producto, Subtipo_producto, Estado_producto, Producto

# Register your models here.
admin.site.register(Tipo_producto)
admin.site.register(Subtipo_producto)
admin.site.register(Estado_producto)
admin.site.register(Producto)

