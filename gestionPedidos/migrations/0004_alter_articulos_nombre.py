# Generated by Django 5.0.2 on 2024-02-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_alter_articulos_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='NombreArticulo'),
        ),
    ]
