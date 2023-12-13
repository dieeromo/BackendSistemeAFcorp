from rest_framework import serializers
from .models import FacturasV, DetalleFacturaV


class FacturasV_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    cliente = serializers.CharField(source='cliente.nombre', read_only = True)
    empresa = serializers.CharField(source='empresa.empresa', read_only = True)
    modo_cv = serializers.CharField(source='modo_cv.modo_cv', read_only = True)


    class Meta:
        model = FacturasV
        fields = "__all__"

class DetalleFacturaV_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    factura = serializers.CharField(source='factura.numero', read_only=True)
    producto = serializers.CharField(source='producto.codigo', read_only=True)
    bodega = serializers.CharField(source='bodega.bodega', read_only=True)
    class Meta:
        model = DetalleFacturaV
        fields = '__all__'
