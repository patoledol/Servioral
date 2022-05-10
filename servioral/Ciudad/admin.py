from django.contrib import admin
from Ciudad.models import ciudad

# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ciudad, CiudadAdmin)
