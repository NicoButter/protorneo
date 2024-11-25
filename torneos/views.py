from django.shortcuts import render, redirect
from .models import Torneo
from pruebas.models import Prueba
from .forms import TorneoForm

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
