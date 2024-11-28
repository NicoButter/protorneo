from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/home.html')


def user_login(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si el usuario es autenticado correctamente, loguearlo
            login(request, user)
            # Redirigir a la página de inicio o a la página de destino
            return redirect('home')  # Reemplaza 'home' con el nombre de la vista que desees
        else:
            # Si las credenciales no son correctas, mostrar un mensaje de error
            return render(request, 'accounts/login.html', {'error': 'Credenciales incorrectas'})

    else:
        # Si el método es GET, simplemente mostrar el formulario de login
        return render(request, 'accounts/login.html')