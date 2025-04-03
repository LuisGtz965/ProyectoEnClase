"""
URL configuration for proyectito project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Módulo para el panel de administración de Django
from django.urls import path # Módulo para definir rutas (URLs) en la aplicación
from aplicacioncita import views # Importa las vistas definidas en la aplicación 'aplicacioncita'

# Ruta para agregar datos (ej: /add/), asociada a la vista 'add' (nombre interno 'add')
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('add/', views.add, name='add'),
    path('update/', views.update_email, name='update_email'),  # Ruta para actualizar el email (ej: /update/), asociada a la vista 'update_email' (nombre 'update_email')
    path('authenticate/', views.authentication, name='authenticate'),     # Ruta para autenticar usuarios (ej: /authenticate/), asociada a la vista 'authentication' (nombre 'authenticate')
    path('logout/', views.logout_view, name='logout'),     # Ruta para cerrar sesión (ej: /logout/), asociada a la vista 'logout_view' (nombre 'logout')
    path('', views.form, name='form'),     # Ruta principal (página de inicio, ej: /), asociada a la vista 'form' (nombre 'form')
    path('usuarios/', views.usuario, name='usuarios'),     # Ruta para gestionar o listar usuarios (ej: /usuarios/), asociada a la vista 'usuario' (nombre 'usuarios')
]
