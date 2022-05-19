from django.db import models
from Documento.models import documento
from Paciente.models import paciente

# Create your models here.

class acudiente(models.Model):

    id_acudiente = models.AutoField(primary_key=True, verbose_name="Id acudiente")
    name = models.CharField(max_length=200, null=False, verbose_name="Nombre del acudiente")
    Documento = models.ForeignKey(documento, null= True, blank= True, on_delete=models.CASCADE )
    paciente = models.ForeignKey(paciente, null=False, verbose_name="Paciente/Acompañante", on_delete=models.CASCADE )
    phone = models.IntegerField(null=False, verbose_name="Teléfono")
    email = models.EmailField(max_length=200, verbose_name="Correo electronico")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Acudiente"
        verbose_name_plural = "Acudientes"
                
    def __str__(self):
        return self.name