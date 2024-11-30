from django.db import models
from datetime import datetime


class Prueba(models.Model):
    NIVELES_DIFICULTAD = [
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),
    ]

    nombre = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nombre oficial de la prueba (e.g., Suelo, Viga de equilibrio)"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        help_text="Descripción detallada de la prueba, incluyendo reglas generales"
    )
    duracion_maxima = models.PositiveIntegerField(
        help_text="Duración máxima permitida en segundos",
        default=0
    )
    nivel_dificultad = models.CharField(
        max_length=50,
        choices=NIVELES_DIFICULTAD,
        default='medio',
        help_text="Nivel de dificultad asignado a la prueba según la FIG"
    )
    puntaje_base = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Puntaje base asignado a la prueba según el código de puntuación",
        default=10.00
    )
    deduccion_caida = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Puntos que se restan por una caída",
        default=1.00
    )
    deduccion_ejecucion = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Deducción por cada error técnico o de ejecución",
        default=0.50
    )
    deduccion_tiempo_excedido = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Penalización por exceder el tiempo permitido (por segundo)",
        default=0.10
    )
    imagen_referencia = models.ImageField(
        upload_to='imagenes_pruebas/',
        null=True,
        blank=True,
        help_text="Imagen ilustrativa de la prueba o el aparato"
    )

    fecha_creacion = models.DateTimeField(default="1990-01-01T00:00:00")  # Fecha por defecto en 1990
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def calcular_puntaje_final(self, puntaje_base, errores, tiempo_excedido):
        """
        Calcula el puntaje final de la prueba.
        - `puntaje_base`: Puntaje base antes de deducciones.
        - `errores`: Número de errores técnicos o de ejecución.
        - `tiempo_excedido`: Tiempo excedido en segundos.
        """
        deducciones = (
            errores * self.deduccion_ejecucion +
            tiempo_excedido * self.deduccion_tiempo_excedido
        )
        puntaje_final = puntaje_base - deducciones
        return max(puntaje_final, 0)  # Asegura que no sea negativo.

    def __str__(self):
        return f"{self.nombre} - Nivel: {self.get_nivel_dificultad_display()}"

    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"
        ordering = ['nombre']
