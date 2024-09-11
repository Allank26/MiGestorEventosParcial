# Generated by Django 5.1.1 on 2024-09-10 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organizador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("telefono", models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("fecha", models.DateField()),
                ("descripcion", models.TextField()),
                (
                    "organizador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eventos.organizador",
                    ),
                ),
            ],
        ),
    ]
