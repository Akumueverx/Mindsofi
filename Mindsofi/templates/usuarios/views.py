from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Guardamos el usuario pero sin confirmar en la DB todavía
            user = form.save(commit=False)
            # Asignamos los datos extra del formulario a los campos del usuario
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save() # Ahora sí, guardamos todo en la base de datos
            login(request, user)
            messages.success(request, "¡Registro exitoso! Has iniciado sesión.")
            # Redirección simple sin namespace
            return redirect('dashboard_admin') 
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'usuarios/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_admin')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_admin')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            # El formulario no es válido, los errores se mostrarán en la plantilla
            messages.error(request, "Por favor, introduce un usuario y contraseña válidos.")
    else:
        form = CustomAuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login')

def dashboard_admin_view(request):
    # Esta vista simplemente renderiza la plantilla base del panel de administración.
    return render(request, 'usuarios/admin/admin_base.html')