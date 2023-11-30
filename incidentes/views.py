from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import Nivel_Serializer, Red_Serializer, Nodo_Serializer, TipoIncidente_Serializer, Incidente_Serializer

from .serializers import Equipos_red_Serializer, Mantenimientos_Equipos_Serializer, Movimiento_Equipos_Serializer

from.models import Nivel, Red, Nodo, TipoIncidente, Incidente

from.models import Equipos_red, Mantenimientos_equipos, Movimientos_equipos


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listNivel(request):
    niveles = Nivel.objects.filter()
    serializer = Nivel_Serializer(niveles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listRed(request):
    redes = Red.objects.filter()
    serializer = Red_Serializer(redes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listNodo(request):
    nodos = Nodo.objects.filter()
    serializer = Nodo_Serializer(nodos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lisTipoIncidente(request):
    tipos_incidentes = TipoIncidente.objects.filter()
    serializer = TipoIncidente_Serializer(tipos_incidentes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroIncidentes(request,pkNivel,pkRed, pkNodo,pkTipo):
    nivel = Nivel.objects.get(id=pkNivel)
    red = Red.objects.get(id=pkRed)
    nodo = Nodo.objects.get(id=pkNodo)
    tipo = TipoIncidente.objects.get(id=pkTipo)
    data = request.data
    user = request.user
    print("peticion hecha")
    try:
        reg_incidente = Incidente.objects.create(
            inicio = data['inicio'],
            fin = data['fin'],
            nivel = nivel,
            red = red,
            nodo = nodo,
            tipo = tipo,
            afectados = data['afectados'],
            descripcion = data['descripcion'],
            user = user
        )
        serializer = Incidente_Serializer(reg_incidente, many=False)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listIncidente(request):
    incidentes = Incidente.objects.filter().order_by('-inicio') 
    serializer = Incidente_Serializer(incidentes, many=True)
    return Response(serializer.data)




########### BITACORA EQUIPOS
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroEquipos(request,pkNodo_inicial, pkNodo_actual):
    nodo_inicial = Nodo.objects.get(id=pkNodo_inicial)
    nodo_actual = Nodo.objects.get(id=pkNodo_actual)
    data = request.data
    user = request.user
    try:
        reg_equipo = Equipos_red.objects.create(
            codigo = data['codigo'],
            descripcion = data['descripcion'],
            alias = data['alias'],
            fecha_instalacion = data['fecha_instalacion'],
            nodo_inicial = nodo_inicial,
            nodo_actual = nodo_actual,
            activo = data['activo'],
            user = user
        )
        serializer = Equipos_red_Serializer(reg_equipo, many=False)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listEquiposRed(request):
    equiposRed = Equipos_red.objects.filter().order_by('-fecha_instalacion') 
    serializer = Equipos_red_Serializer(equiposRed, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroMantenimientoEquipos(request,pkEquipo):
    equipo = Equipos_red.objects.get(id=pkEquipo)
    data = request.data
    user = request.user
    try:
        reg_mantenimiento = Mantenimientos_equipos.objects.create(
            equipo = equipo,
            fecha = data['fecha'],
            problema = data['problema'],
            solucion = data['solucion'],
            user = user
        )
        serializer = Mantenimientos_Equipos_Serializer(reg_mantenimiento, many=False)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroMovimiento_Equipos(request,pkEquipo, pkNodoSalida, pkNodoLlegada):
    nodo_salida = Nodo.objects.get(id=pkNodoSalida)
    nodo_llegada = Nodo.objects.get(id=pkNodoLlegada)
    equipo = Equipos_red.objects.get(id=pkEquipo)
    data = request.data
    user = request.user
    try:
        reg_movimientos = Movimientos_equipos.objects.create(
            equipo = equipo,
            fecha = data['fecha'],
            nodo_salida = nodo_salida,
            nodo_llegada = nodo_llegada,
            observacion = data['observacion'],
            user = user
        )
        serializer = Movimiento_Equipos_Serializer(reg_movimientos, many=False)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
