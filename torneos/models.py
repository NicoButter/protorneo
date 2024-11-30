from django.db import models
from pruebas.models import Prueba
from accounts.models import Usuario  # Asumimos que el jefe de torneo es un tipo de usuario

#-------------------------------------------------------------------------------------------------------------------------------------

class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    sede = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, choices=[('junior', 'Junior'), ('senior', 'Senior'), ('nivel1', 'Nivel 1'), ('nivel2', 'Nivel 2')], blank=True, null=True)
    reglamento = models.FileField(upload_to='reglamentos/', blank=True, null=True)  # Subida de PDF para el reglamento
    fecha_limite_participantes = models.DateTimeField()  # Fecha límite para cargar participantes
    cronograma = models.TextField(blank=True, null=True)  # Cronograma del evento
    jefe_torneo = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'jefe_torneo'})
    pruebas = models.ManyToManyField(Prueba, related_name='torneos', blank=True)
    
    def __str__(self):
        return self.nombre

#-------------------------------------------------------------------------------------------------------------------------------------

class Delegacion(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='delegaciones')
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'profesor'})
    nombre_delegacion = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nombre_delegacion} - {self.profesor}"

#-------------------------------------------------------------------------------------------------------------------------------------

class Participante(models.Model):
    delegacion = models.ForeignKey(Delegacion, on_delete=models.CASCADE, related_name='participantes')
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, choices=[('junior', 'Junior'), ('senior', 'Senior')])  # Categoría del participante
    
    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

#-------------------------------------------------------------------------------------------------------------------------------------

class AsignacionJuez(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='asignaciones')
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, related_name='asignaciones')
    juez = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'juez'})
    
    def __str__(self):
        return f"{self.juez} asignado a {self.prueba} en {self.torneo}"