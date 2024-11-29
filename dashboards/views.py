from django.shortcuts import render
from torneos.models import Torneo, AsignacionJuez
from accounts.models import Usuario
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

def is_jefe_torneo(user):
    return user.is_authenticated and user.rol == 'jefe_torneo'

@user_passes_test(is_jefe_torneo)
def dashboard_jefe_torneo(request):
    return render(request, 'dashboards/dashboard_jefe_torneo.html')
