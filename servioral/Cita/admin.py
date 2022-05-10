from django.contrib import admin
from Cita.models import cita

# Register your models here.

class CitaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(cita, CitaAdmin)
