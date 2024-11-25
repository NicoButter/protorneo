# urls.py en la app 'dashboards'
from django.urls import path
from . import views

urlpatterns = [
    path('juez/', views.dashboard_juez, name='dashboard_juez'),
    # Otras rutas para los dashboards de los otros usuarios
]
