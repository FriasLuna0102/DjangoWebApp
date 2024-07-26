from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitudForm, FormularioRegistroCorreo, SolicitudUpdateForm
from .models import Solicitud
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test

# Redirección en la raíz según el estado de autenticación
def root_redirect(request):
    print("Entro aqui")
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('solicitudes:gestionar_solicitudes')  # Redirige al listado de todas las solicitudes si es superusuario
        else:
            return redirect('solicitudes:crear_solicitud')  # Redirige a la creación de solicitud si es un usuario normal
    else:
        return redirect('login')  # Redirige al login si no está autenticado

# Vista para crear una solicitud
@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return redirect('solicitudes:listar_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/crear_solicitudes.html', {'form': form})

# Vista para listar solicitudes según el usuario
@login_required
def listar_solicitudes(request):
    if request.user.is_superuser:
        solicitudes = Solicitud.objects.all()
    else:
        solicitudes = Solicitud.objects.filter(usuario=request.user)
    return render(request, 'solicitudes/listar_solicitudes.html', {'solicitudes': solicitudes})

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistroCorreo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al inicio de sesión después del registro
    else:
        form = FormularioRegistroCorreo()
    return render(request, 'registration/registro.html', {'form': form})

# Vista para el login de usuarios
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('root_redirect')  # Redirige a la vista raíz después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Decorador personalizado para verificar si el usuario es agente
def is_agent(user):
    return user.is_staff  # Verifica si el usuario pertenece al grupo de agentes

# Vista para gestionar todas las solicitudes, accesible solo para agentes
@user_passes_test(is_agent)
def gestionar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'solicitudes/gestionar_solicitudes.html', {'solicitudes': solicitudes})

# Vista para editar una solicitud, accesible solo para agentes
@user_passes_test(is_agent)
def editar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        form = SolicitudUpdateForm(request.POST, request.FILES, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('solicitudes:gestionar_solicitudes')
    else:
        form = SolicitudUpdateForm(instance=solicitud)
    return render(request, 'solicitudes/editar_solicitudes.html', {'form': form})


@login_required
def ver_comentario(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    return render(request, 'solicitudes/ver_comentario.html', {'solicitud': solicitud})