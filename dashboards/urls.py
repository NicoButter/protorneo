from django.urls import path
from . import views

urlpatterns = [
    path('dashboard_jefe_torneo/', views.dashboard_jefe_torneo, name='dashboard_jefe_torneo'),

    # Otras rutas para los dashboards de los otros usuarios
]
