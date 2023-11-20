from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import Nivel_Serializer, Red_Serializer, Nodo_Serializer, TipoIncidente_Serializer, Incidente_Serializer

from.models import Nivel, Red, Nodo, TipoIncidente, Incidente


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
    print(serializer.data)
    return Response(serializer.data)
