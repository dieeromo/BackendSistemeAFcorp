from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import Cobros_facturas_serializer
from . models import Cobros_facturas
from facturasVentas.models import FacturasV
from generalAFC.models import Caja_empresa, Empresa_corp


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroCobroFacturaV(request,pk_factura,pk_empresa):
    factura = FacturasV.objects.get(id=pk_factura)
    
    empresa = Empresa_corp.objects.get(id=pk_empresa)
    data = request.data
    user = request.user

    caja = Caja_empresa.objects.get(user=user)
 
    try:
        reg_cobroFactura = Cobros_facturas.objects.create(
            factura = factura,
            fecha = data['fecha'],
            monto_pago = data['monto_pago'],
            monto_capital = data['monto_capital'],
            monto_interes = data['monto_interes'],
            saldo_anterior = data['saldo_anterior'],
            saldo_actual = data['saldo_actual'],
            caja = caja,
            empresa = empresa,
            observacion = data['observacion']
            #empresa = empresa,

        )
        serializer = Cobros_facturas_serializer(reg_cobroFactura, many=False)

        return Response(serializer.data)
    except:
        message = {'detalle': 'algo esta mal en el registro del cliente'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listCobrosFacturasVentas(request):
    cobros = Cobros_facturas.objects.filter().order_by('-fecha') 
    serializer = Cobros_facturas_serializer(cobros, many=True)
    return Response(serializer.data)

