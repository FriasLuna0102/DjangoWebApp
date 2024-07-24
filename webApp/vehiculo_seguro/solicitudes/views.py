from django.shortcuts import render, redirect
from .forms import SolicitudForm
from django.contrib.auth.decorators import login_required

from .models import Solicitud


@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            print(solicitud.MATRICULA)
            print(solicitud)
            print("Es valido")
            solicitud.save()
            return redirect('solicitudes:listar_solicitudes')
    else:
        form = SolicitudForm()
        print("No es valido")
    print("Fuera")
    return render(request, 'solicitudes/crear_solicitudes.html', {'form': form})

@login_required
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'solicitudes/listar_solicitudes.html', {'solicitudes': solicitudes})
