from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

from .serializers import FacturasV_Serializer, DetalleFacturaV_Serializer
from .models import FacturasV, DetalleFacturaV
from generalAFC.models import Modo_CompraVenta, Empresa_corp, Bodega
from clientes.models import Cliente
from productos.models import Producto


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroFacturaDetalleV(request,pk_factura,pk_producto,pk_bodega):
    factura = FacturasV.objects.get(id=pk_factura)
    producto_salida = Producto.objects.get(id=pk_producto)
    bodega_salida = Bodega.objects.get(id=pk_bodega)
    #empresa = Empresa_corp.objects.get(id=pk_empresa)
    data = request.data
    user = request.user
    print("peticion hecha")
    try:
        reg_detalleFactura = DetalleFacturaV.objects.create(
            factura = factura,
            producto = producto_salida,
            precio = data['precio'],
            cantidad = data['cantidad'],
            subtotal = data['subtotal'],
            total = data['total'],
            user = user,
            bodega = bodega_salida,
            #empresa = empresa,

        )
        serializer = DetalleFacturaV_Serializer(reg_detalleFactura, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroFacturaV(request, pk_cliente, pk_modo_cv, pk_empresa):
    cliente = Cliente.objects.get(id=pk_cliente)
    modo_cv = Modo_CompraVenta.objects.get(id=pk_modo_cv)
    empresa = Empresa_corp.objects.get(id=pk_empresa)
    data = request.data
    user = request.user
    print("peticion hecha")
    print(cliente)
    print(modo_cv)
    print(empresa)
    print(user)
    print('monto')
    print(data['monto'])
    try:
        reg_factura = FacturasV.objects.create(
            numero = data['numero'],
            fecha = data['fecha'],
            cliente = cliente,
            modo_cv = modo_cv,
            user = user,
            empresa = empresa,
            ##estado_pago = False,
            #estado pago por defecto viene F, se modifica en cobros de facturas
            monto = data['monto'],
            saldo = data['saldo'],  #### OJO: se modifica en cobros
            #saldo = '',
            plazo_meses = data['plazo_meses'],
            observacion = data['observacion'],
            #factura_cerrada = False
        )
        serializer = FacturasV_Serializer(reg_factura, many=False)
        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listFacturasVentas(request):
    facturas_ventas = FacturasV.objects.filter().order_by('-fecha') 
    serializer = FacturasV_Serializer(facturas_ventas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUltimaFactura(request):
    try:
        ultimo_dato = FacturasV.objects.filter().order_by('id').last()
    except FacturasV.DoesNotExist:
        ultimo_dato = None

    print(ultimo_dato.id)
    if ultimo_dato is not None:
        #serializer = FacturasV_Serializer(ultimo_dato, many=True)
        
        #return Response(serializer.data)
        return JsonResponse({'id_factura':ultimo_dato.id})
    else:
        return  JsonResponse({'id_factura': None})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allUltimaFactura(request):
    try:
        ultimo_dato = FacturasV.objects.filter().order_by('id').last()
        print(ultimo_dato.numero)
    except FacturasV.DoesNotExist:
        ultimo_dato = None
    if ultimo_dato is not None:
        serializer = FacturasV_Serializer(ultimo_dato, many=False)
        
        return Response(serializer.data)
        #return JsonResponse({'id':ultimo_dato.id, })
    else:
        return  JsonResponse({'factura': None})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detallesUltimaFactura(request, id):
    try:
        ultimo_dato = DetalleFacturaV.objects.filter(factura=id)
 
    except DetalleFacturaV.DoesNotExist:
        ultimo_dato = None
    if ultimo_dato is not None:
        serializer = DetalleFacturaV_Serializer(ultimo_dato, many=True)
        
        return Response(serializer.data)
        #return JsonResponse({'id':ultimo_dato.id, })
    else:
        return  JsonResponse({'detalle': None})
