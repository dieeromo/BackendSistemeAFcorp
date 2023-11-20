from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



from .serializers import FacturasV_Serializer
from .models import FacturasV
from generalAFC.models import Modo_CompraVenta, Empresa_corp
from clientes.models import Cliente

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registroFacturaV(request,pk_cliente,pk_modo_cv, pk_empresa):
    cliente = Cliente.objects.get(id=pk_cliente)
    modo_cv = Modo_CompraVenta.objects.get(id=pk_modo_cv)
    empresa = Empresa_corp.objects.get(id=pk_empresa)
    data = request.data
    user = request.user
    print("peticion hecha")
    try:
        reg_factura = FacturasV.objects.create(
            numero = data['numero'],
            fecha = data['fecha'],
            cliente = cliente,
            modo_cv = modo_cv,
            user = user,
            empresa = empresa,
            estado_pago = False,
            #estado pago por defecto viene F, se modifica en cobros de facturas
            #monto = data['monto'],
            monto = '',
            #saldo = data['saldo'],  #### OJO: se modifica en cobros
            saldo = '',
            #plazo_meses = data['plazo_meses'],
            plazo_meses = 6,
            observacion = data['observacion'],
            factura_cerrada = False
        )
        serializer = FacturasV_Serializer(reg_factura, many=False)
        print("despues de crear")
        print(serializer.data)
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
