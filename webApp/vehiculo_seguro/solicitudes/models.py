from django.db import models
from django.contrib.auth.models import User

class Solicitud(models.Model):
    MATRICULA = 'M'
    CHASIS = 'C'
    VIN = 'V'
    TIPO_VEHICULO_CHOICES = [
        (MATRICULA, 'Matrícula'),
        (CHASIS, 'Número de Chasis'),
        (VIN, 'Número de VIN'),
    ]

    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_vehiculo = models.CharField(max_length=1, choices=TIPO_VEHICULO_CHOICES)
    numero_identificacion = models.CharField(max_length=50)
    nombre_solicitante = models.CharField(max_length=100)
    email_solicitante = models.EmailField()
    archivo_matricula = models.FileField(upload_to='archivos/matriculas/')
    archivo_licencia = models.FileField(upload_to='archivos/licencias/')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    comentario = models.TextField(blank=True, null=True)
    numero_poliza = models.CharField(max_length=100, blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    fecha_expiracion = models.DateField(blank=True, null=True)
    carnet_seguro = models.ImageField(upload_to='archivos/carnets/', blank=True, null=True)

    def __str__(self):
        return f'Solicitud {self.id} - {self.nombre_solicitante}'
