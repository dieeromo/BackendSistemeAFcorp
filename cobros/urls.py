from django.urls import path
from . import views

urlpatterns = [
    path('registro/<int:pk_factura>/<int:pk_empresa>/', views.registroCobroFacturaV),
    path('listcobros/',views.listCobrosFacturasVentas)
]