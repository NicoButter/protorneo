# models.py en la app 'torneos'
from django.db import models
from pruebas.models import Prueba  # Importando el modelo Prueba de la app 'pruebas'

class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    pruebas = models.ManyToManyField(Prueba, related_name='torneos', blank=True)
    
    def __str__(self):
        return self.nombre