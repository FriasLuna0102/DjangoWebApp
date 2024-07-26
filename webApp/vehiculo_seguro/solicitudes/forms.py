from django import forms
from .models import Solicitud
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo_vehiculo', 'numero_identificacion', 'nombre_solicitante', 'email_solicitante', 'archivo_matricula', 'archivo_licencia']

class SolicitudUpdateForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['estado', 'comentario', 'numero_poliza', 'fecha_emision', 'fecha_expiracion', 'carnet_seguro']
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
            'fecha_expiracion': forms.DateInput(attrs={'type': 'date'}),
        }

class FormularioRegistroCorreo(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
