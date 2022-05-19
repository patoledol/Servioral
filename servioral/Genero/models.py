from django.db import models

# Create your models here.

class genero(models.Model):

    genero =  models.CharField(max_length=200, null=False, verbose_name="Genero", choices= (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ))
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
                
    def __str__(self):
        return self.genero