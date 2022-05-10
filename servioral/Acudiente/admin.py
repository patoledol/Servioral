from django.contrib import admin
from Acudiente.models import acudiente

# Register your models here.

class AcudienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(acudiente, AcudienteAdmin)
