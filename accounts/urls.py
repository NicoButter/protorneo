from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Otras rutas como login, register...
]
