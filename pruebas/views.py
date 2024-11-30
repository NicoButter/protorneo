from django.shortcuts import render
from .models import Prueba

def listar_pruebas(request):
    pruebas = Prueba.objects.all()
    return render(request, 'listar_pruebas.html', {'pruebas': pruebas})
