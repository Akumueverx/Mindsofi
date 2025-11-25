# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Ficha, Programa


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "rol",
            "first_name",
            "last_name",
            "documento",
            "telefono",
            "edad",
            "genero",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clases bootstrap a widgets por defecto
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                # Aplicar clase 'form-select' a todos los campos de selección
                field.widget.attrs.update({"class": "form-select"})
            else:
                field.widget.attrs.update({"class": "form-control"})

        # Hacemos que programa y ficha no sean obligatorios en el formulario
        if 'programa' in self.fields:
            self.fields['programa'].required = False
        if 'ficha' in self.fields:
            self.fields['ficha'].required = False

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

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['numero', 'programa', 'jornada', 'fecha_inicio', 'fecha_fin', 'cupo_maximo']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['programa'].widget.attrs.update({'class': 'form-select'})
        self.fields['jornada'].widget.attrs.update({'class': 'form-select'})
        self.fields['cupo_maximo'].widget.attrs.update({'class': 'form-control', 'type': 'number', 'min': '1'})

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'nivel']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})

        # Convertir el campo 'nivel' en un selector para consistencia
        self.fields['nivel'].widget = forms.Select(choices=[
            ('', 'Seleccione un nivel'),
            ('Técnico', 'Técnico'),
            ('Tecnólogo', 'Tecnólogo'),
            ('Auxiliar', 'Auxiliar'),
            ('Complementario', 'Complementario'),
            ('Especialización Tecnológica', 'Especialización Tecnológica'),
        ])
        self.fields['nivel'].widget.attrs.update({'class': 'form-select'})

class UsuarioAdminForm(forms.ModelForm):
    """
    Formulario para que un administrador edite los datos de un usuario.
    """
    class Meta:
        model = Usuario
        fields = [
            'username', 'first_name', 'last_name', 'email', 'rol', 
            'documento', 'telefono', 'edad', 'genero', 
            'programa', 'ficha', 'especialidad', 'cargo', 'is_active'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({"class": "form-select"})
            elif isinstance(field.widget, forms.CheckboxInput):
                 field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})
        
        # Hacemos que los campos condicionales no sean obligatorios por defecto
        self.fields['programa'].required = False
        self.fields['ficha'].required = False
        self.fields['especialidad'].required = False
        self.fields['cargo'].required = False

    def clean_documento(self):
        documento = self.cleaned_data.get("documento")
        if documento:
            qs = Usuario.objects.filter(documento=documento)
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
