from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuario

# Formulario de cambio de usuario
class UsuarioChangeForm(UserChangeForm):
    # Este formulario maneja el cambio de usuario, sin permitir la edición directa de la contraseña.
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'rol', 'especialidad', 'foto', 'is_active')
    
    def clean_password(self):
        # Si no se ha proporcionado una nueva contraseña, no la cambiamos.
        return self.initial["password"]

