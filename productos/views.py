from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import TipoProducto_Serializer, SubtipoProducto_Serializer, EstadoProducto_Serializer, Producto_Serializer

