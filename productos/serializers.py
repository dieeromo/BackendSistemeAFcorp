from rest_framework import serializers
from .models import Tipo_producto, Subtipo_producto, Estado_producto, Producto

class TipoProducto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_producto
        fields = "__all__"

class SubtipoProducto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subtipo_producto
        fields = "__all__"
        
class EstadoProducto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_producto
        fields = "__all__"

class Producto_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    tipo = serializers.CharField(source='tipo.tipo', read_only=True)
    subtipo = serializers.CharField(source='subtipo.subtipo', read_only=True)
    estado = serializers.CharField(source='estado.estado', read_only=True)
    class Meta:
        model = Producto
        fields = "__all__"

