# Generated by Django 5.1.1 on 2024-09-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0002_remove_organizador_telefono_evento_ubicacion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="organizador",
            name="telefono",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
