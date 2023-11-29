from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import date

from .serializers import TipoProducto_Serializer, SubtipoProducto_Serializer, EstadoProducto_Serializer, Producto_Serializer

from .models import Tipo_producto, Subtipo_producto, Estado_producto, Producto



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listTipoProducto(request):
    tipoProducto = Tipo_producto.objects.filter()
    serializer = TipoProducto_Serializer(tipoProducto, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listSubTipoProducto(request):
    subTipoProducto = Subtipo_producto.objects.filter()
    serializer = SubtipoProducto_Serializer(subTipoProducto, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listEstadoProducto(request):
    estadoProducto = Estado_producto.objects.filter()
    serializer = EstadoProducto_Serializer(estadoProducto, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroProductos(request,pk_tipo,pk_subtipo, pk_estado):
    tipo = Tipo_producto.objects.get(id=pk_tipo)
    subtipo = Subtipo_producto.objects.get(id=pk_subtipo)
    estado = Estado_producto.objects.get(id=pk_estado)
    data = request.data
    user = request.user

    try:
        reg_producto = Producto.objects.create(
            modelo = data['modelo'],
            descripcion = data['descripcion'],
            codigo = data['codigo'],

            tipo = tipo,
            subtipo = subtipo,
            estado = estado,

            precio_entrada = data['precio_entrada'],
            precio_salida = data['precio_salida'],
            precio_promo = data['precio_promo'],
            seguimiento = data['seguimiento'],
            observacion = data['observacion'],
            fecha_modificacion = date.today(),
            user = user,

        )
        serializer = Producto_Serializer(reg_producto, many=False)
        print("despues de crear")
        print(serializer.data)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listProducto(request):
    producto = Producto.objects.filter()
    serializer = Producto_Serializer(producto, many=True)
    return Response(serializer.data)