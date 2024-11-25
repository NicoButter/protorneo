from django.urls import path
from . import views

app_name = 'torneos'

urlpatterns = [
    path('crear/', views.crear_torneo, name='crear_torneo'),
    #path('lista/', views.lista_torneos, name='lista_torneos'),
]
