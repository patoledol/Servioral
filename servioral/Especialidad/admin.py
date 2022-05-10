from django.contrib import admin
from Especialidad.models import especialidad


# Register your models here.

class EspecialidadAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(especialidad, EspecialidadAdmin)
