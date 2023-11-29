from django.urls import path
from . import views

urlpatterns = [
    path('list_tipo_producto/', views.listTipoProducto),
    path('list_subtipo_producto/', views.listSubTipoProducto),
    path('list_estado_producto/', views.listEstadoProducto),
    path('register/<int:pk_tipo>/<int:pk_subtipo>/<int:pk_estado>/', views.registroProductos),

    path('list_producto/', views.listProducto),

]