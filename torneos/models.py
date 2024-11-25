from django.db import models
from pruebas.models import Prueba
from accounts.models import JefeDeTorneo, Juez  # Asumimos que el jefe de torneo es un tipo de usuario

#-------------------------------------------------------------------------------------------------------------------------------------

class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    jefe_de_torneo = models.ForeignKey(JefeDeTorneo, on_delete=models.CASCADE)
    pruebas = models.ManyToManyField(Prueba, related_name='torneos', blank=True)
    
    def __str__(self):
        return self.nombre

#-------------------------------------------------------------------------------------------------------------------------------------

class AsignacionJuez(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='asignaciones')
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, related_name='asignaciones')
    juez = models.ForeignKey(Juez, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.juez} asignado a {self.prueba} en {self.torneo}"