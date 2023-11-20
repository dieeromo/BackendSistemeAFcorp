from rest_framework import serializers
from .models import Nivel, Red,  Nodo, TipoIncidente, Incidente

class Nivel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = "__all__"

class Red_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Red
        fields = "__all__"

class Nodo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nodo
        fields = "__all__"

class TipoIncidente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIncidente
        fields = "__all__"

class Incidente_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    nivel = serializers.CharField(source='nivel.nivel', read_only=True)
    red = serializers.CharField(source='red.red', read_only=True)
    nodo = serializers.CharField(source='nodo.nodo', read_only=True)
    tipo = serializers.CharField(source='tipo.tipo', read_only=True)
    class Meta:
        model = Incidente
        fields = "__all__"