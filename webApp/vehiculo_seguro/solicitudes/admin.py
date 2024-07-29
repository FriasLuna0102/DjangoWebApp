from django.contrib import admin

from .models import Solicitud

# Registro de la vista de administración de solicitudes
@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('tipo_vehiculo', 'numero_identificacion', 'nombre_solicitante', 'email_solicitante', 'estado', 'fecha_emision', 'fecha_expiracion')
    list_filter = ('estado',)
    search_fields = ('tipo_vehiculo', 'numero_identificacion', 'nombre_solicitante', 'email_solicitante')
    ordering = ('fecha_emision',)
