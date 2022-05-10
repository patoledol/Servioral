from django.contrib import admin
from Documento.models import documento

# Register your models here.

class DocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(documento, DocumentoAdmin)
