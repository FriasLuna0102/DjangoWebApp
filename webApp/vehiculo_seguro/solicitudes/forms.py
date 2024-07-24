from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo_vehiculo', 'numero_identificacion', 'nombre_solicitante', 'email_solicitante', 'archivo_matricula', 'archivo_licencia']
