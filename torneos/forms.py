from django import forms
from .models import Torneo, AsignacionJuez
from accounts.models import Usuario
from pruebas.models import Prueba

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre', 'fecha', 'sede', 'categoria', 'reglamento', 'fecha_limite_participantes', 'pruebas']

    # Agregar un campo para seleccionar las pruebas asociadas al torneo
    pruebas = forms.ModelMultipleChoiceField(
        queryset=Prueba.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

#-----------------------------------------------------------------------------------------------------------------------

class AsignacionJuezForm(forms.ModelForm):
    # Aquí limitamos los jueces a los que tienen el rol 'juez'
    juez = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(rol='juez'),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = AsignacionJuez
        fields = ['torneo', 'prueba', 'juez']
