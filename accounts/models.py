from django.contrib.auth.models import AbstractUser
from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
#--------------------------------------------------------------------------------------------------------------------------------------

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('jefe_torneo', 'Jefe de Torneo'),
        ('juez', 'Juez de Especialidad'),
        ('profesor', 'Profesor'),
        ('participante', 'Participante'),
    )
    
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    
    # Otros campos que consideres necesarios como teléfono, dirección, etc.
    
    def __str__(self):
        return self.username
    
#--------------------------------------------------------------------------------------------------------------------------------------

class Legajo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='legajos')
    numero_legajo = models.CharField(max_length=50, unique=True)  # El número único de legajo
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    comentarios = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='legajos/', null=True, blank=True)  # Para documentos relacionados

    def __str__(self):
        return f"Legajo {self.numero_legajo} - {self.usuario}"

#--------------------------------------------------------------------------------------------------------------------------------------

class Telefono(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='telefonos')
    tipo = models.CharField(max_length=50, choices=[('personal', 'Personal'), ('trabajo', 'Trabajo')])
    numero = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.tipo} - {self.numero}"
    
#--------------------------------------------------------------------------------------------------------------------------------------

class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')
    tipo = models.CharField(max_length=50, choices=[('residencial', 'Residencial'), ('trabajo', 'Trabajo')])
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tipo} - {self.direccion}"

#--------------------------------------------------------------------------------------------------------------------------------------    

class Correo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='correos')
    tipo = models.CharField(max_length=50, choices=[('personal', 'Personal'), ('trabajo', 'Trabajo')])
    correo = models.EmailField()

    def __str__(self):
        return f"{self.tipo} - {self.correo}"

#--------------------------------------------------------------------------------------------------------------------------------------