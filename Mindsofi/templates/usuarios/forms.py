from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Un formulario para crear usuarios, con el campo de email requerido.
    """
    first_name = forms.CharField(max_length=30, required=True, label="Nombres")
    last_name = forms.CharField(max_length=30, required=True, label="Apellidos")
    email = forms.EmailField(required=True, help_text='Requerido. Se necesita un correo válido.')

    class Meta(UserCreationForm.Meta):
        model = User
        # El orden aquí define el orden en el formulario
        fields = ('username', 'first_name', 'last_name', 'email')

class CustomAuthenticationForm(AuthenticationForm):
    """
    Un formulario de autenticación personalizado para añadir clases de Bootstrap.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})