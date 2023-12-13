# Generated by Django 3.2.16 on 2023-12-08 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturasVentas', '0007_alter_detallefacturav_empresa'),
        ('generalAFC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobros_facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('monto_capital', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('monto_interes', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('saldo_anterior', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('saldo_actual', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('observacion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generalAFC.caja_empresa')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generalAFC.empresa_corp')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturasVentas.facturasv')),
            ],
        ),
    ]
