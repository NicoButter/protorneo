from django.shortcuts import render
from torneos.models import Torneo, AsignacionJuez
from accounts.models import Usuario
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

def is_juez(user):
    return user.is_authenticated and user.rol == 'juez'

@user_passes_test(is_juez)
def dashboard_jefe_torneo(request):
    # Lógica que quieras agregar para el dashboard de juez
    return render(request, 'dashboards/dashboard_jefe_torneo.html')
