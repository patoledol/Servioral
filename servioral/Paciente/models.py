from datetime import datetime


import datetime
from django.db import models
from Documento.models import documento
from Ciudad.models import ciudad
from Genero.models import genero

# Create your models here.

class paciente(models.Model):

    id_paciente = models.AutoField(primary_key=True, verbose_name="Id paciente")
    name = models.CharField(max_length=200, null=False, verbose_name="Nombre")
    document = models.ForeignKey(documento, null= True, blank= True, on_delete=models.CASCADE, verbose_name="Documento")
    num_documento = models.IntegerField(null=False, verbose_name="Número de documento")
    city = models.ForeignKey(ciudad, null= True, blank= True, on_delete=models.CASCADE, verbose_name="Ciudad")
    phone = models.IntegerField(null=False, verbose_name="Número de teléfono")
    email = models.EmailField(max_length=200, null=False, verbose_name="Correo electronico")
    birth_date = datetime.datetime.now()
    formatedDay  = birth_date.strftime("%Y/%m/%d")
    gender = models.ForeignKey(genero, null= True, blank= True, on_delete=models.CASCADE, verbose_name="Género")
    tto = models.TextField(max_length=200, null=True ,verbose_name="Tratamiento")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
                
    def __str__(self):
        return self.name