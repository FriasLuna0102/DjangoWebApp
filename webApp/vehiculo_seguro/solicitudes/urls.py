from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'solicitudes'  # Define el nombre del espacio de nombres aquí


urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('listar/', views.listar_solicitudes, name='listar_solicitudes'),
    path('registro/', views.registro, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
