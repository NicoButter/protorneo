from django.shortcuts import render
from torneos.models import Torneo, AsignacionJuez
from accounts.models import Juez
from django.utils import timezone


def dashboard_juez(request):
    juez = request.user.juez  # Suponiendo que el usuario es un juez
    asignaciones = AsignacionJuez.objects.filter(juez=juez)
    torneos_activos = [asignacion.torneo for asignacion in asignaciones if asignacion.torneo.fecha >= timezone.now()]

    return render(request, 'dashboards/dashboard_juez.html', {'torneos_activos': torneos_activos})
