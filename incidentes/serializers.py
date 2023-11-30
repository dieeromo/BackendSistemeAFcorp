from rest_framework import serializers
from .models import Nivel, Red,  Nodo, TipoIncidente, Incidente
from .models import Equipos_red, Mantenimientos_equipos, Movimientos_equipos

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


class Equipos_red_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    nodo_inicial = serializers.CharField(source='nodo_inicial.nodo', read_only=True)
    nodo_actual = serializers.CharField(source='nodo_actual.nodo', read_only=True)
    class Meta:
        model = Equipos_red
        fields = "__all__"

class Mantenimientos_Equipos_Serializer(serializers.ModelSerializer):
    equipo = serializers.CharField(source='equipo.equipo', read_only=True)
    class Meta:
        mode = Mantenimientos_equipos
        fields = "__all__"


class Movimiento_Equipos_Serializer(serializers.ModelSerializer):
    equipo = serializers.CharField(source='equipo.equipo', read_only=True)
    nodo_salida = serializers.CharField(source='nodo_salida.nodo_salida', read_only=True)
    nodo_llegada = serializers.CharField(source='nodo_llegada.nodo_llegada', read_only=True)
    class Meta:
        mode = Movimientos_equipos
        fields = "__all__"