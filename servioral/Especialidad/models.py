from django.db import models

# Create your models here.

class especialidad(models.Model):

    id_especialidad = models.AutoField(primary_key=True, verbose_name="Id odontologo")
    name_es = models.CharField(max_length=200, null=False, verbose_name="Nombre de la especialidad")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
                
    def __str__(self):
        return self.name_es