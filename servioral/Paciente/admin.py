from django.contrib import admin
from Paciente.models import paciente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(paciente, PacienteAdmin)
