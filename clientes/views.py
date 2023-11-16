from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente
from .serializers import ClienteSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroCliente(request):
    data = request.data
    try:
        cliente = Cliente.objects.create(
            nombre = data['nombre'],
            direccion = data['direccion'],
            telefono1 = data['telefono1'],
            telefono2 = data['telefono2'],
            user = request.user,
            observacion = data['observacion']
        )
        print(cliente.nombre)
        print(cliente.user)
        serializer = ClienteSerializer(cliente, many=False)
        print("hbdhjbsda")
        print(serializer)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listClientes(request):
    clientes = Cliente.objects.filter().order_by('-fecha') 
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroCliente(request):
    data = request.data

    cliente = Cliente.objects.create(
        nombre = data['nombre'],
        direccion = data['direccion'],
        telefono1 = data['telefono1'],
        telefono2 = data['telefono2'],
        user = request.user,
        observacion = data['observacion']
        )
    print(cliente.nombre)
    print(cliente.user)
    serializer = ClienteSerializer(cliente, many=False)
    print("hbdhjbsda")
    return Response(serializer.data)
"""