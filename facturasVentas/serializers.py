from rest_framework import serializers
from .models import FacturasV


class FacturasV_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    cliente = serializers.CharField(source='cliente.nombre', read_only = True)
    empresa = serializers.CharField(source='empresa.empresa', read_only = True)
    modo_cv = serializers.CharField(source='modo_cv.modo_cv', read_only = True)


    class Meta:
        model = FacturasV
        fields = "__all__"
