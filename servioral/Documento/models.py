from django.db import models

# Create your models here.


class documento (models.Model):

    tipoDocu = models.CharField(max_length=200, null=False, verbose_name="Tipo de documento", choices= (
        ('Registro civil', 'Registro civil'),
        ('Tarjeta de identidad', 'Tarjeta de identidad'),
        ('Cédula de ciudadania', 'Cédula de ciudadania'),
        ('Cédula de extrangeria', 'Cédula de extrangeria'),
        ('Pasaporte', 'Pasaporte'),
    ))
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
                
    def __str__(self):
        return self.tipoDocu