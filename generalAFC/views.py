
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from . serializars import Empresa_corp_Serializer, Caja_empresa_Serializer, Modo_CompraVenta_Serializer, Bodega_Serializer

from . models import Empresa_corp, Caja_empresa, Modo_CompraVenta, Bodega

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEmpresa_corp(request):
    empresa = Empresa_corp.objects.filter()
    serializer = Empresa_corp_Serializer(empresa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCaja_empresa(request):
    caja = Caja_empresa.objects.filter()
    serializer = Caja_empresa_Serializer(caja, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getModoCompraVenta(request):
    modo_cv = Modo_CompraVenta.objects.filter()
    serializer = Modo_CompraVenta_Serializer(modo_cv, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBodega(request):
    bodega = Bodega.objects.filter()
    serializer = Bodega_Serializer(bodega, many=True)
    return Response(serializer.data)