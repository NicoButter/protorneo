from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import UsuarioLoginForm
from django.contrib import messages



def home(request):
    return render(request, 'accounts/home.html')


def user_login(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirigir según el rol del usuario
                if user.rol == 'jefe_torneo':  # Cambia esto según el valor del rol de juez
                    return redirect('dashboard_jefe_torneo')  # Nombre de la URL para el dashboard del juez
                else:
                    return redirect('default_dashboard')  # Redirigir a otro dashboard o página
            else:
                messages.error(request, 'Credenciales inválidas')
    else:
        form = UsuarioLoginForm()

    return render(request, 'accounts/login.html', {'form': form})