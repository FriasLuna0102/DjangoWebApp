from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'solicitudes'

urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('listar/', views.listar_solicitudes, name='listar_solicitudes'),
    path('registro/', views.registro, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gestionar/', views.gestionar_solicitudes, name='gestionar_solicitudes'),
    path('editar/<int:pk>/', views.editar_solicitud, name='editar_solicitud'),
    path('ver_comentario/<int:pk>/', views.ver_comentario, name='ver_comentario'),  # Nueva URL
]
