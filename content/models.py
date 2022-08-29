from uuid import uuid4
from django.db import models

# Create your models here.

class Sistema(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField("Descripción")
    api_key = models.CharField("Api Key", default=uuid4, unique=True, max_length=100)

    class Meta:
        verbose_name = "sistema"
        verbose_name_plural = "sistemas"

    def __str__(self):
        return self.nombre


class Archivo(models.Model):
    id = models.CharField("id", max_length=50, primary_key=True)
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField("Descripción")
    sistemas = models.ManyToManyField(Sistema)
    file = models.FileField("Archivo", upload_to=f'archivos/', max_length=100)
    validar_api_key = models.BooleanField("Validar API Key", default=True)

    class Meta:
        verbose_name = "archivo"
        verbose_name_plural = "archivos"

    def __str__(self):
        return self.nombre

