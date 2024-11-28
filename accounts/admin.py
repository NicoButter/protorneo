from django.contrib import admin
from .models import Especialidad, Usuario, Legajo, Telefono, Direccion, Correo

# Registro del modelo Especialidad
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Campos que se mostrarán en la lista de objetos
    search_fields = ('nombre',)  # Habilitar búsqueda por nombre

# Registro del modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'rol', 'especialidad', 'foto')  # Campos que se mostrarán en la lista de objetos
    list_filter = ('rol', 'especialidad')  # Filtros disponibles en el admin
    search_fields = ('username', 'email')  # Habilitar búsqueda por nombre de usuario y correo

# Registro del modelo Legajo
@admin.register(Legajo)
class LegajoAdmin(admin.ModelAdmin):
    list_display = ('numero_legajo', 'usuario', 'fecha_creacion', 'estado', 'archivo')  # Campos que se mostrarán
    list_filter = ('estado', 'fecha_creacion')  # Filtros disponibles
    search_fields = ('numero_legajo',)  # Habilitar búsqueda por número de legajo

# Registro del modelo Telefono
@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'numero')  # Campos que se mostrarán
    search_fields = ('numero',)  # Habilitar búsqueda por número de teléfono

# Registro del modelo Direccion
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'direccion', 'ciudad', 'estado', 'codigo_postal')  # Campos que se mostrarán
    search_fields = ('direccion', 'ciudad', 'estado')  # Habilitar búsqueda por dirección, ciudad y estado

# Registro del modelo Correo
@admin.register(Correo)
class CorreoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'correo')  # Campos que se mostrarán
    search_fields = ('correo',)  # Habilitar búsqueda por correo electrónico
