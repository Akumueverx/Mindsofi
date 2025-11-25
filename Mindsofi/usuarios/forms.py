# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "rol",
            "first_name", # Añadido
            "last_name",  # Añadido
            "documento",
            "telefono",
            "edad",       # Añadido
            "genero",     # Añadido
            "programa",
            "ficha",
            "especialidad",
            "cargo",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clases bootstrap a widgets por defecto
        for name, field in self.fields.items():
            if name in ["rol", "genero", "programa", "ficha"]:
                # Aplicar clase 'form-select' a todos los campos de selección
                field.widget.attrs.update({"class": "form-select"})
            else:
                field.widget.attrs.update({"class": "form-control"})

        # Quitar help_text molestos (opcional)
        if "username" in self.fields:
            self.fields["username"].help_text = None

    def clean_documento(self):
        documento = self.cleaned_data.get("documento")
        if documento:
            qs = Usuario.objects.filter(documento=documento)
            # Si es edición de usuario (instance) permitir mismo documento
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya existe un usuario con ese número de documento.")
        return documento


class CustomAuthenticationForm(AuthenticationForm):
    """
    AuthenticationForm con clases bootstrap para inputs.
    Puedes usar esta clase en tus vistas en vez de AuthenticationForm
    si quieres que los campos tengan la clase 'form-control'.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
