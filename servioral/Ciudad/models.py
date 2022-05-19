from email.headerregistry import Address
from django.db import models

# Create your models here.

class ciudad(models.Model):

    ciudad = models.CharField(max_length=200, null=False, verbose_name="Nombre de ciudad", choices= (
        ('Armenia', 'Armenia'),
        ('Barrancabermeja', 'Barrancabermeja'),
        ('Barranquilla', 'Barranquilla'),
        ('Bogotá', 'Bogotá'),
        ('Bucaramanga', 'Bucaramanga'),
        ('Buga', 'Buga'),
        ('Cali', 'Cali'),
        ('Cartagena', 'Cartagena'),
        ('Chía', 'Chía'),
        ('Cúcuta', 'Cúcuta'),
        ('Duitama', 'Duitama'),
        ('Florencia', 'Florencia'),
        ('Fusagasugá', 'Fusagasugá'),
        ('Girardot', 'Girardot'),
        ('Honda', 'Honda'),
        ('Ibagué', 'Ibagué'),
        ('Ipiales', 'Ipiales'),
        ('Jamundí', 'Jamundí'),
        ('Leticia', 'Leticia'),
        ('Manizales', 'Manizales'),
        ('Mariquita', 'Mariquita'),
        ('Medellín', 'Medellín'),
        ('Mompox', 'Mompox'),
        ('Montería', 'Montería'),
        ('Murillo', 'Murillo'),
        ('Neiva', 'Neiva'),
        ('Pamplona', 'Pamplona'),
        ('Pasto', 'Pasto'),
        ('Pereira', 'Pereira'),
        ('Popayán', 'Popayán'),
        ('Riohacha', 'Riohacha'),
        ('San Andrés y Providencia', 'San Andrés y Providencia'),
        ('San Antero', 'San Antero'),
        ('Santa Marta', 'Santa Marta'),
        ('Santafé de Antioquia', 'Santafé de Antioquia'),
        ('Sevilla','Sevilla'),
        ('Sincelejo', 'Sincelejo'),
        ('Sogamoso', 'Sogamoso'),
        ('Tabio', 'Tabio'),
        ('Tocancipá', 'Tocancipá'),
        ('Tolú', 'Tolú'),
        ('Tuluá', 'Tuluá'),
        ('Tumaco', 'Tumaco')

    ))
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
                
    def __str__(self):
        return self.ciudad