from django.contrib import admin
from Genero.models import genero

# Register your models here.

class GeneroAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(genero, GeneroAdmin)
