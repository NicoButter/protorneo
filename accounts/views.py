from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse



def home(request):
    return render(request, 'accounts/home.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Obtener el usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Realizar login
                auth_login(request, user)
                print(f"Usuario {user.username} autenticado y sesión iniciada.")
                
                # Mostrar un mensaje de éxito
                messages.success(request, 'Has iniciado sesión correctamente.')
                
                # Verificar si existe un parámetro 'next' para redirigir al usuario
                next_url = request.GET.get('next')
                print(f"next_url: {next_url}")
                
                if not next_url:  # Si no hay parámetro 'next', redirigir según el rol
                    if user.rol == 'jefe_torneo':
                        next_url = reverse('dashboard_jefe_torneo')  # Usar reverse para obtener la URL
                    elif user.rol == 'juez':
                        next_url = reverse('dashboard_juez')
                    elif user.rol == 'profesor':
                        next_url = reverse('dashboard_profesor')
                    elif user.rol == 'participante':
                        next_url = reverse('dashboard_participante')
                    else:
                        next_url = reverse('home')  # Redirigir a home por defecto
                
                print(f"Redirigiendo a: {next_url}")
                return redirect(next_url)  # Redirigir al usuario según el rol o a la URL 'next'

            else:
                # Si el usuario no es encontrado, mostrar un mensaje de error
                messages.error(request, 'Credenciales inválidas.')

        else:
            # Si el formulario no es válido, mostrar un mensaje genérico de error
            messages.error(request, 'Formulario incorrecto. Verifica tus credenciales.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

