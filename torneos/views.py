from django.shortcuts import render, redirect
from .models import Torneo, AsignacionJuez
from pruebas.models import Prueba
from .forms import TorneoForm, AsignarJuezForm

def crear_torneo(request):
    if request.method == 'POST':
        form = TorneoForm(request.POST)
        if form.is_valid():
            torneo = form.save()
            # Aquí podrías asociar las pruebas seleccionadas al torneo
            return redirect('torneos:lista_torneos')
    else:
        form = TorneoForm()
    
    pruebas = Prueba.objects.all()
    return render(request, 'torneos/crear_torneo.html', {'form': form, 'pruebas': pruebas})


def asignar_juez_a_prueba(request, torneo_id):
    torneo = Torneo.objects.get(id=torneo_id)
    if request.method == 'POST':
        form = AsignarJuezForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la asignación
            return redirect('torneos:ver_torneo', torneo_id=torneo.id)
    else:
        form = AsignarJuezForm(initial={'torneo': torneo})
    
    return render(request, 'torneos/asignar_juez.html', {'form': form, 'torneo': torneo})
