from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from aplicacioncita.models import Usuarios
from django.shortcuts import redirect

def usuario_form(request: HttpRequest):
    return render(request, 'agregaruser.html')

def usuario(request: HttpRequest):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre: str = request.POST['nombre']
        edad: float = float(request.POST['edad'])
        correo_electronico: str = request.POST['correo_electronico']

        # Crear y guardar el nuevo usuario
        nuevo_usuario = Usuarios.objects.create(
            nombre=nombre,
            edad=edad,
            correo_electronico=correo_electronico
        )

    # Obtener todos los usuarios para mostrar en la plantilla
    usuarios = Usuarios.objects.all()
    return render(request, 'agregaruser.html', {'usuarios': usuarios})

def form(request):
    if request.method == 'POST':
        username: str = request.POST['username']
        pswd: str = request.POST['password']
        user: User = authenticate(request, username=username, password=pswd)
        if username is not None:
            login(request, user)
            return HttpResponse('Usuario Autenticado')
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')

def add(response):
    User.objects.create_user('lcgr6', 'luis@gmail.com', '1234')
    return HttpResponse('Datos guardados satisfactoriamente')

def update_email(response):
    u = User.objects.get(username='Polarsito')
    u.email = 'polar@outlook.com'
    u.save()
    return HttpResponse('Datos actualizados satisfactoriamente')

def authentication(response):
    username: str = response.POST['username']
    password: str = response.POST['password']
    if username and password:
        u = authenticate(response, username=username, password=password)
    if u:
        login(response, u)
        return HttpResponse('Usuario Autenticado')
    return HttpResponse('Usuario no autenticado')

def logout_view(request):
    logout(request)
    return HttpResponse('Usuario deslogueado')