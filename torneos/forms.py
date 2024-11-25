from django import forms
from .models import Torneo, AsignacionJuez
from accounts.models import Juez


class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre', 'fecha', 'lugar', 'pruebas']

#-----------------------------------------------------------------------------------------------------------------------

class AsignarJuezForm(forms.ModelForm):
    class Meta:
        model = AsignacionJuez
        fields = ['torneo', 'prueba', 'juez']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitar los jueces disponibles solo a los jueces activos
        self.fields['juez'].queryset = Juez.objects.filter(activo=True)

#-----------------------------------------------------------------------------------------------------------------------