from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registroCliente),
    path('list/', views.listClientes),
]
