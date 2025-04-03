from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from aplicacioncita.models import Usuarios
from django.shortcuts import redirect

# Vista para mostrar el formulario de agregar usuario (no procesa datos POST)
def usuario_form(request: HttpRequest):
    """Renderiza la plantilla 'agregaruser.html' sin lógica adicional."""
    return render(request, 'agregaruser.html')


# Vista para manejar la creación de usuarios y listarlos
def usuario(request: HttpRequest):
    """Procesa el formulario de usuario (POST) y muestra la lista de usuarios."""
    if request.method == 'POST':
        # Obtener datos del formulario POST
        nombre: str = request.POST['nombre']
        edad: float = float(request.POST['edad'])
        correo_electronico: str = request.POST['correo_electronico']

        # Crear y guardar un nuevo usuario en la base de datos
        nuevo_usuario = Usuarios.objects.create(
            nombre=nombre,
            edad=edad,
            correo_electronico=correo_electronico
        )

    # Obtener todos los usuarios (tanto para GET como POST)
    usuarios = Usuarios.objects.all()
    return render(request, 'agregaruser.html', {'usuarios': usuarios})


# Vista para el formulario de autenticación (login)
def form(request):
    """Maneja el login de usuarios: autentica y redirige o muestra errores."""
    if request.method == 'POST':
        username: str = request.POST['username']
        pswd: str = request.POST['password']
        user: User = authenticate(request, username=username, password=pswd)
        
        if user is not None:  # Si las credenciales son válidas
            login(request, user)
            return HttpResponse('Usuario Autenticado')
        else:
            return render(request, 'index.html')  # Muestra el formulario con error implícito
    
    # Renderiza el formulario inicial (GET)
    return render(request, 'index.html')


# Vista para crear un usuario de prueba (hardcodeado)
def add(response):
    """Crea un usuario de prueba con datos fijos (uso para pruebas)."""
    User.objects.create_user('lcgr6', 'luis@gmail.com', '1234')
    return HttpResponse('Datos guardados satisfactoriamente')


# Vista para actualizar el email de un usuario específico
def update_email(response):
    """Actualiza el email del usuario con username 'Polarsito'."""
    u = User.objects.get(username='Polarsito')
    u.email = 'polar@outlook.com'
    u.save()
    return HttpResponse('Datos actualizados satisfactoriamente')


# Vista para autenticar usuarios (similar a 'form', pero con respuesta HTTP)
def authentication(response):
    """Autentica al usuario y devuelve una respuesta HTTP (sin redirección)."""
    username: str = response.POST['username']
    password: str = response.POST['password']
    
    if username and password:
        u = authenticate(response, username=username, password=password)
    
    if u:  # Si la autenticación fue exitosa
        login(response, u)
        return HttpResponse('Usuario Autenticado')
    
    return HttpResponse('Usuario no autenticado')  # Si falla


# Vista para cerrar sesión
def logout_view(request):
    """Cierra la sesión del usuario actual."""
    logout(request)
    return HttpResponse('Usuario deslogueado')