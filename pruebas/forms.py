from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'nivel_dificultad': forms.Select(attrs={'class': 'custom-select'}),
        }
        help_texts = {
            'descripcion': 'Proporcione detalles adicionales sobre la prueba.',
        }