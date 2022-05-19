import imp
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from Especialidad.models import especialidad

# Create your models here.

class odontologo(models.Model):

    id_odontologo = models.AutoField(primary_key=True, verbose_name="Id odontologo")
    name = models.CharField(max_length=50, null=False, verbose_name="Nombre")
    phone = models.IntegerField(null=False, verbose_name="Teléfono")
    especialidad = models.ForeignKey(especialidad, null= True, blank= True, on_delete=models.CASCADE, verbose_name="Especialidad")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    
    class Meta:
        verbose_name = "Odontologo"
        verbose_name_plural = "Odontologos"
                
    def __str__(self):
        return self.name
