from django.urls import path
from . import views

urlpatterns = [
    path('registro/<int:pk_cliente>/<int:pk_modo_cv>/<int:pk_empresa>/', views.registroFacturaV),
    path('list/', views.listFacturasVentas),

]