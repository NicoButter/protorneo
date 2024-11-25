from django.urls import path
from . import views

app_name = 'torneos'

urlpatterns = [
    path('crear/', views.crear_torneo, name='crear_torneo'),
    path('<int:torneo_id>/asignar_juez/', views.asignar_juez_a_prueba, name='asignar_juez'),
]
