from rest_framework import serializers
from . models import Cobros_facturas

class Cobros_facturas_serializer(serializers.ModelSerializer):
    factura = serializers.CharField(source='factura.numero', read_only = True)
    caja = serializers.CharField(source='caja.caja', read_only = True)
    empresa = serializers.CharField(source='empresa.empresa', read_only = True)
    
    class Meta:
        model = Cobros_facturas
        fields = "__all__"


