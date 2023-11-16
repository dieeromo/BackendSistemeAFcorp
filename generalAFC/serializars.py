from rest_framework import serializers
from .models import Empresa_corp, Caja_empresa, Modo_CompraVenta, Bodega 

class Empresa_corp_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa_corp
        fields = "__all__"

class Caja_empresa_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Caja_empresa
        fields = "__all__"

class Modo_CompraVenta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Modo_CompraVenta
        fields = "__all__"

class Bodega_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = "__all__"


