from django.db import models

# Create your models here.

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Agregar este campo

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=255, default='')
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, related_name='eventos')
    descripcion = models.TextField(null=True, blank=True)  # Agrega el campo 'descripcion'

    def __str__(self):
        return self.nombre
    