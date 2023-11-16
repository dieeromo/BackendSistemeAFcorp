

from django.urls import path
from . import views

urlpatterns = [
    path('getempresa_corp/', views.getEmpresa_corp),
    path('getcaja_empresa/', views.getCaja_empresa),
    path('getmodocompra_venta/', views.getModoCompraVenta),
    path('getbodega/', views.getBodega),

]