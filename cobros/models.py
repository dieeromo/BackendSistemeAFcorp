from django.db import models
from users.models import User
from facturasVentas.models import FacturasV
from generalAFC.models import Caja_empresa, Empresa_corp

# Create your models here.

class Cobros_facturas(models.Model):
    factura = models.ForeignKey(FacturasV, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    monto_capital = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    monto_interes = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    saldo_actual = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    caja = models.ForeignKey(Caja_empresa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa_corp, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=200,null=True, blank= True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

