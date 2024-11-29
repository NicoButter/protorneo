from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Especialidad, Usuario, Legajo, Telefono, Direccion, Correo


# Formulario para la creación de usuarios
class UsuarioForm(UserCreationForm):
    # Define los campos que se desean mostrar en el formulario de creación
    rol = forms.ChoiceField(choices=Usuario.ROL_CHOICES, required=True)
    especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all(), required=False)
    foto = forms.ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'rol', 'especialidad', 'foto')



@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Inline para Legajo
class LegajoInline(admin.TabularInline):
    model = Legajo
    extra = 1  # Formularios vacíos adicionales para agregar legajos

# Inline para Teléfono
class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 1  # Formularios vacíos adicionales para agregar teléfonos

# Inline para Dirección
class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1  # Formularios vacíos adicionales para agregar direcciones

# Inline para Correo
class CorreoInline(admin.TabularInline):
    model = Correo
    extra = 1  # Formularios vacíos adicionales para agregar correos

# Administrador de Usuario
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm  # Usar el formulario de edición personalizado
    add_form = UsuarioForm  # Usar el formulario de creación personalizado

    # Campos que aparecerán en el administrador
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'especialidad', 'foto', 'is_active')
    list_filter = ('rol', 'especialidad', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Configuración de campos visibles al editar el usuario
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'rol', 'especialidad', 'foto', 'is_active')
        }),
        ('Contraseña', {
            'fields': ('password',),  # La contraseña no se edita directamente
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'rol', 'especialidad', 'foto'),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:  # Si estamos editando un usuario existente
            # Cuando estamos editando un usuario, la contraseña no se muestra como campo editable,
            # sino que Django muestra un enlace para cambiarla.
            fieldsets = list(fieldsets)
            fieldsets[0][1]['fields'] = ('username', 'email', 'first_name', 'last_name', 'rol', 'especialidad', 'foto', 'is_active')
            fieldsets.append(('Contraseña', {
                'fields': ('password',),
            }))
        return fieldsets

# Administrador de Legajo
@admin.register(Legajo)
class LegajoAdmin(admin.ModelAdmin):
    list_display = ('numero_legajo', 'usuario', 'fecha_creacion', 'estado', 'archivo')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('numero_legajo',)

# Administrador de Teléfono
@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'numero')
    search_fields = ('numero',)

# Administrador de Dirección
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'direccion', 'ciudad', 'estado', 'codigo_postal')
    search_fields = ('direccion', 'ciudad', 'estado')

# Administrador de Correo
@admin.register(Correo)
class CorreoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'correo')
    search_fields = ('correo',)
