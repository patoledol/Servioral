import imp, datetime
from django.db import models
from Odontologo.models import odontologo
from Especialidad.models import especialidad
from Paciente.models import paciente

# Create your models here.

class cita(models.Model):

    status=models.BooleanField(default=False, verbose_name="Aceptada")
    id_cita = models.AutoField(primary_key=True, verbose_name="Id acudiente")
    paciente = models.ForeignKey(paciente, null= True, blank= True, on_delete=models.CASCADE, verbose_name="Paciente" )
    id_doc = models.ForeignKey(odontologo, null= True, blank= True, on_delete=models.CASCADE, verbose_name="Doctor" )
    espe = models.ForeignKey(especialidad,null= True, blank= True, on_delete=models.CASCADE, verbose_name="Especialidad" )
    day = datetime.datetime.now()
    formatedDay  = day.strftime("%Y/%m/%d")
    date = models.DateTimeField()
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    
    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
                
    # def __str__(self):
    #     return self.name
