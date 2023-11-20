# Generated by Django 3.2.16 on 2023-11-17 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Nodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIncidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('afectados', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentes.nivel')),
                ('nodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentes.nodo')),
                ('red', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentes.red')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentes.tipoincidente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
