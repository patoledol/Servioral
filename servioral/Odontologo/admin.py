from django.contrib import admin
from Odontologo.models import odontologo

# Register your models here.

# class ContactAdmin(admin.ModelAdmin):
#     readonly_fields = ('procedure','name', 'mail', 'phone', 'message', 'created')
#     list_filter = ('procedure', 'status')
#     list_display = ('name','procedure', 'status')

class OdontologoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(odontologo, OdontologoAdmin)
