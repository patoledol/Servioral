import imp, datetime
from django.db import models
from Odontologo.models import odontologo
# Create your models here.

class cita(models.Model):

    id_cita = models.AutoField(primary_key=True, verbose_name="Id acudiente")
    id_doc = models.ForeignKey(odontologo, null= True, blank= True, on_delete=models.CASCADE )
    day = datetime.datetime.now()
    formatedDay  = day.strftime("%Y/%m/%d")
    date = models.DateTimeField()
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    
    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
                
    def __str__(self):
        return self.name