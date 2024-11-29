from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from .models import Usuario

# Formulario de cambio de usuario
class UsuarioChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'rol', 'especialidad', 'foto')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer que el campo de la contraseña sea opcional
        if not self.instance.pk:
            self.fields['password'].required = True
        else:
            self.fields['password'].required = False


# Formulario de login
class UsuarioLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    
    class Meta:
        fields = ('username', 'password')
