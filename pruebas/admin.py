from django.contrib import admin
from .models import Prueba
from .forms import PruebaForm

@admin.register(Prueba)
class PruebaAdmin(admin.ModelAdmin):
    form = PruebaForm
    list_display = ('nombre', 'nivel_dificultad', 'duracion_maxima', 'puntaje_base', 'fecha_actualizacion')
    list_filter = ('nivel_dificultad', 'fecha_actualizacion')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'descripcion', 'imagen_referencia')
        }),
        ('Detalles Técnicos', {
            'fields': ('duracion_maxima', 'nivel_dificultad', 'puntaje_base', 'deduccion_caida', 'deduccion_ejecucion', 'deduccion_tiempo_excedido')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',),
        }),
    )
    