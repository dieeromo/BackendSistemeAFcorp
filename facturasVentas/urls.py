from django.urls import path
from . import views

urlpatterns = [
    path('registro/<int:pk_cliente>/<int:pk_modo_cv>/<int:pk_empresa>/', views.registroFacturaV),
    path('list/', views.listFacturasVentas),
    
    path('registro_detalle/<int:pk_factura>/<int:pk_producto>/<int:pk_bodega>/', views.registroFacturaDetalleV),
    path('get_ultima/', views.getUltimaFactura),
    path('all_ultima/', views.allUltimaFactura),
    path('detalles_ultima/<int:id>/', views.detallesUltimaFactura),
]