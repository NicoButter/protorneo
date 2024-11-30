from django.shortcuts import render, redirect
from .models import Torneo, AsignacionJuez
from pruebas.models import Prueba
from .forms import TorneoForm, AsignarJuezForm

def crear_torneo(request):
    if request.method == 'POST':
        form = TorneoForm(request.POST, request.FILES)
        if form.is_valid():
            torneo = form.save(commit=False)
            torneo.jefe_torneo = request.user  # Asignar el jefe de torneo (el usuario logueado)
            torneo.save()  # Guardar el torneo
            form.save_m2m()  # Guardar las pruebas asociadas
            return redirect('dashboard_jefe_torneo')  # Redirigir a la página del jefe de torneo
    else:
        form = TorneoForm()

    return render(request, 'crear_torneo.html', {'form': form})


def asignar_juez_a_prueba(request, torneo_id):
    torneo = Torneo.objects.get(id=torneo_id)
    if request.method == 'POST':
        form = AsignarJuezForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la asignación
            return redirect('torneos:ver_torneo', torneo_id=torneo.id)
    else:
        # Al crear el formulario, se pasa el torneo de forma explícita
        form = AsignarJuezForm(initial={'torneo': torneo})

    return render(request, 'torneos/asignar_juez.html', {'form': form, 'torneo': torneo})
