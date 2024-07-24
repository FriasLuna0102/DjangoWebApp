from django import forms
from .models import Solicitud
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo_vehiculo', 'numero_identificacion', 'nombre_solicitante', 'email_solicitante', 'archivo_matricula', 'archivo_licencia']


class FormularioRegistroCorreo(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

