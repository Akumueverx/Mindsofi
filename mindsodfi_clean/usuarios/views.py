# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UsuarioCreationForm, CustomAuthenticationForm
from .models import Usuario
from .decorators import role_required


def register_view(request):
    if request.method == "POST":
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("redirect_dashboard")
    else:
        form = UsuarioCreationForm()
    return render(request, "usuarios/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("redirect_dashboard")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def redirect_dashboard(request):
    # Un superusuario siempre debe ir al dashboard de admin
    if request.user.is_superuser:
        return redirect("dashboard_admin")

    rol_dashboard_map = {
        "aprendiz": "dashboard_aprendiz",
        "instructor": "dashboard_instructor",
        "administrativo": "dashboard_admin",
    }
    dashboard_url_name = rol_dashboard_map.get(request.user.rol)
    
    if dashboard_url_name:
        return redirect(dashboard_url_name)
    return redirect("login")


@login_required
@role_required(allowed_roles=['aprendiz'])
def dashboard_aprendiz(request):
    return render(request, "usuarios/aprendiz/dashboard.html")


@login_required
@role_required(allowed_roles=['instructor'])
def dashboard_instructor(request):
    return render(request, "usuarios/instructor/dashboard.html")


@login_required
@role_required(allowed_roles=['administrativo'])
def dashboard_admin(request):
    return render(request, "usuarios/admin/dashboard.html") # La URL es /dashboard/admin/


# --- Vistas para el Panel del Instructor (ya existentes) ---
# @login_required
# @role_required(allowed_roles=['instructor', 'administrativo'])
# def instructor_fichas_view(request):
#     return render(request, 'usuarios/instructor/instructor_fichas.html')
# ... (otras vistas de instructor)


# --- Vistas para el Panel del Aprendiz ---
@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_programa_view(request):
    return render(request, 'usuarios/aprendiz/programa.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_ficha_view(request):
    return render(request, 'usuarios/aprendiz/ficha.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_horario_view(request):
    return render(request, 'usuarios/aprendiz/horario.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_calificaciones_view(request):
    return render(request, 'usuarios/aprendiz/calificaciones.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_instructores_view(request):
    return render(request, 'usuarios/aprendiz/instructores.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_cursos_view(request):
    return render(request, 'usuarios/aprendiz/cursos.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_noticias_view(request):
    return render(request, 'usuarios/aprendiz/noticias.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_soporte_view(request):
    return render(request, 'usuarios/aprendiz/soporte.html')


# --- Vistas para el Panel del Admin ---
@login_required
@role_required(allowed_roles=['administrativo'])
def admin_usuarios_view(request):
    return render(request, 'usuarios/admin/aprendices.html') # Asumiendo que 'aprendices.html' es para gestión de usuarios

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_programas_view(request):
    return render(request, 'usuarios/admin/programas.html')

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_fichas_view(request):
    return render(request, 'usuarios/admin/fichas.html')

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_reportes_view(request):
    return render(request, 'usuarios/admin/reportes.html')


# --- Vistas para el Panel del Instructor ---
@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_fichas_view(request):
    return render(request, 'usuarios/instructor/instructor_fichas.html')

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_programa_view(request):
    return render(request, 'usuarios/instructor/instructor_programa.html')

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_horarios_view(request):
    return render(request, 'usuarios/instructor/instructor_horarios.html')

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_anuncios_view(request):
    return render(request, 'usuarios/instructor/instructor_anuncios.html')

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_reportes_view(request):
    return render(request, 'usuarios/instructor/instructor_reportes.html')
