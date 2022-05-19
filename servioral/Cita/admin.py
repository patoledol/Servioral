from django.contrib import admin
from Cita.models import cita

# Register your models here.

class CitaAdmin(admin.ModelAdmin):
    readonly_fields = ('id_doc', 'paciente','espe', 'date','hour', 'created', 'updated')
    list_filter = ('id_cita', 'status')
    list_display = ('id_doc', 'status')

admin.site.register(cita, CitaAdmin)
