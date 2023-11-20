from django.db import models
from users.models import User
from clientes.models import Cliente
from generalAFC.models import Modo_CompraVenta, Empresa_corp




class FacturasV(models.Model):
    numero = models.CharField(max_length=50)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modo_cv = models.ForeignKey(Modo_CompraVenta, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa_corp, on_delete=models.CASCADE)
    estado_pago = models.BooleanField(default=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank= True)
    plazo_meses = models.IntegerField(null=True, blank= True)
    observacion = models.CharField(max_length=200,null=True, blank= True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    factura_cerrada = models.BooleanField(default=False)
