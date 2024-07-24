from django.shortcuts import render, redirect
from .forms import SolicitudForm
from django.contrib.auth.decorators import login_required

from .models import Solicitud

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

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


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('some_view')  # Cambia a tu vista principal
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})