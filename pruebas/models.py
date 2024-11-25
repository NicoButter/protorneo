from django.db import models

class Prueba(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.PositiveIntegerField(help_text="Duración en segundos de la prueba", default=0)
    nivel_dificultad = models.CharField(
        max_length=50,
        choices=[('bajo', 'Bajo'), ('medio', 'Medio'), ('alto', 'Alto')],
        default='medio'
    )
    imagen = models.ImageField(upload_to='imagenes_pruebas/', null=True, blank=True)

    def __str__(self):
        return self.nombre