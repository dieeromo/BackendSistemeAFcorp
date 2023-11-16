from django.contrib import admin
from . models import Empresa_corp, Caja_empresa, Modo_CompraVenta, Bodega

admin.site.register(Empresa_corp)
admin.site.register(Caja_empresa)
admin.site.register(Modo_CompraVenta)
admin.site.register(Bodega)

