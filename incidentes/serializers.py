from rest_framework import serializers
from .models import Nivel, Red,  Nodo, TipoIncidente, Incidente
from .models import Equipos_red, Mantenimientos_equipos, Movimientos_equipos
from .models import Tipo_fibra, Trazado_FO, Tipo_trabajo, Trabajos_FO
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

## BITACORA EQUIPOS
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
        model = Mantenimientos_equipos
        fields = "__all__"


class Movimiento_Equipos_Serializer(serializers.ModelSerializer):
    equipo = serializers.CharField(source='equipo.equipo', read_only=True)
    nodo_salida = serializers.CharField(source='nodo_salida.nodo_salida', read_only=True)
    nodo_llegada = serializers.CharField(source='nodo_llegada.nodo_llegada', read_only=True)
    class Meta:
        mode = Movimientos_equipos
        fields = "__all__"

##BITACORA FIBRA OPTICA

class Tipo_fibra_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    class Meta:
        model = Tipo_fibra
        fields = "__all__"

class Trazado_FO_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    tipo_fibra = serializers.CharField(source='tipo_fibra.tipo', read_only=True)
    class Meta:
        model = Trazado_FO
        fields = "__all__"


class Tipo_trabajo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_trabajo
        fields = "__all__"

class Trabajos_FO_Serializer(serializers.ModelSerializer):
    trazado = serializers.CharField(source='trazado.identificador', read_only = True)
    user = serializers.CharField(source='user.user_name', read_only=True)
    tipo_trabajo = serializers.CharField(source='tipo_trabajo.tipo_trabajo', read_only=True)
    tipo_fibra_cambio = serializers.CharField(source='tipo_fibra_cambio.tipo', read_only=True)
    class Meta:
        model = Trabajos_FO
        fields = "__all__"


