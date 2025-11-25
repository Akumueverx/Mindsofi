from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import UsuarioCreationForm, CustomAuthenticationForm, FichaForm, ProgramaForm, UsuarioAdminForm
from .models import Usuario, Ficha, Programa
from .decorators import role_required

# Constante para los ambientes del mapa para reducir la duplicación de código
AMBIENTES_MAPA = [
    {'id': '301', 'nombre': 'Ambiente 301'},
    {'id': '302', 'nombre': 'Ambiente 302'},
    {'id': '303', 'nombre': 'Ambiente 303'},
    {'id': '205', 'nombre': 'Ambiente 205 (Multimedia)'},
    {'id': '101', 'nombre': 'Auditorio'},
    {'id': 'cafeteria', 'nombre': 'Cafetería'},
]



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
    # TODO: Obtener el programa del aprendiz actual desde la BD
    programa_ejemplo = {
        'nombre': 'Análisis y Desarrollo de Software',
        'codigo': '228106',
        'version': '1',
        'nivel': 'Tecnólogo',
        'duracion_meses': 24,
        'descripcion': 'El programa de formación en Análisis y Desarrollo de Software (ADSO) se enfoca en la construcción de soluciones de software, abarcando el ciclo de vida completo del desarrollo, desde el levantamiento de requisitos hasta la implementación y mantenimiento.',
        'competencias': [
            'Diseñar la solución de software de acuerdo con los requisitos del cliente.',
            'Construir el software de acuerdo con el diseño establecido.',
            'Realizar pruebas al software para verificar su funcionamiento.',
            'Implantar la solución de software en el ambiente del cliente.',
            'Promover la interacción idónea consigo mismo, con los demás y con la naturaleza en los contextos laboral y social.'
        ]
    }
    context = {
        'programa': programa_ejemplo
    }
    return render(request, 'usuarios/aprendiz/programa.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_ficha_view(request):
    # TODO: Obtener la ficha del aprendiz actual desde la BD
    ficha_ejemplo = {
        'numero': '2556678',
        'programa_nombre': 'Análisis y Desarrollo de Software',
        'jornada': 'Diurna',
        'fecha_inicio': '2023-02-01',
        'fecha_fin': '2025-02-01',
        'aprendices_count': 30,
    }
    context = {
        'ficha': ficha_ejemplo
    }
    return render(request, 'usuarios/aprendiz/ficha.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_ficha_detalle_view(request):
    # TODO: Obtener la ficha detallada del aprendiz actual desde la BD
    ficha_detalle_ejemplo = {
        'numero': '2556678',
        'programa_nombre': 'Análisis y Desarrollo de Software',
        'jornada': 'Diurna',
        'fecha_inicio': '2023-02-01',
        'fecha_fin': '2025-02-01',
        'aprendices_count': 30,
        'descripcion': 'La ficha 2556678 pertenece al programa de Análisis y Desarrollo de Software, enfocado en formar tecnólogos capaces de diseñar, construir y mantener soluciones de software.',
        'instructor_lider': 'Ricardo Gómez',
        'ubicacion': 'Centro de Formación SENA - Regional Antioquia',
        'competencias': [
            'Diseñar la solución de software de acuerdo con los requisitos del cliente.',
            'Construir el software de acuerdo con el diseño establecido.',
            'Realizar pruebas al software para verificar su funcionamiento.',
            'Implantar la solución de software en el ambiente del cliente.',
            'Promover la interacción idónea consigo mismo, con los demás y con la naturaleza en los contextos laboral y social.'
        ],
        'horarios': [
            {'dia': 'Lunes', 'hora': '08:00 - 12:00', 'competencia': 'Diseño de Interfaces'},
            {'dia': 'Lunes', 'hora': '13:00 - 17:00', 'competencia': 'Desarrollo Front-End'},
            {'dia': 'Miércoles', 'hora': '10:00 - 14:00', 'competencia': 'Bases de Datos'},
            {'dia': 'Jueves', 'hora': '08:00 - 10:00', 'competencia': 'Promover la Interacción Idónea'},
        ],
        'contacto': {
            'telefono': '604 123 4567',
            'email': 'info@sena.edu.co'
        }
    }
    context = {
        'ficha': ficha_detalle_ejemplo
    }
    return render(request, 'usuarios/aprendiz/ficha_detalle.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_horario_view(request):
    # TODO: Reemplazar con la lógica real para obtener el horario del aprendiz
    horario_ejemplo = [
        {'id': 1, 'competencia': 'Diseño de Interfaces', 'instructor': 'Ricardo Gómez', 'programa': 'Análisis y Desarrollo de Software', 'ficha_numero': '2556678', 'dia': 'Lunes', 'hora_inicio': '08:00', 'hora_fin': '12:00', 'ambiente': 'Ambiente 301'},
        {'id': 2, 'competencia': 'Desarrollo Front-End', 'instructor': 'Laura Nuñez', 'programa': 'Análisis y Desarrollo de Software', 'ficha_numero': '2556678', 'dia': 'Lunes', 'hora_inicio': '13:00', 'hora_fin': '17:00', 'ambiente': 'Ambiente 302'},
        {'id': 3, 'competencia': 'Bases de Datos', 'instructor': 'Ricardo Gómez', 'programa': 'Análisis y Desarrollo de Software', 'ficha_numero': '2556678', 'dia': 'Miércoles', 'hora_inicio': '10:00', 'hora_fin': '14:00', 'ambiente': 'Ambiente 301'},
        {'id': 4, 'competencia': 'Promover la Interacción Idónea', 'instructor': 'Sandra Milena', 'programa': 'Análisis y Desarrollo de Software', 'ficha_numero': '2556678', 'dia': 'Jueves', 'hora_inicio': '08:00', 'hora_fin': '10:00', 'ambiente': 'Auditorio'},
    ]

    horarios_por_dia = {}
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    for dia in dias_semana:
        horarios_por_dia[dia] = sorted(
            [h for h in horario_ejemplo if h['dia'] == dia],
            key=lambda x: x['hora_inicio']
        )
    context = {
        'horarios_por_dia': horarios_por_dia
    }
    return render(request, 'usuarios/aprendiz/horario.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_ubicacion_view(request):
    """
    Vista para mostrar la ubicación simulada del aprendiz en un plano.
    """
    # Coordenadas GPS de prueba (porcentaje de la pantalla)
    # En un caso real, esto vendría de un API o un dispositivo.
    posicion_gps = {'x': 25, 'y': 40}  # Ejemplo: 25% desde la izquierda, 40% desde arriba

    ambientes_con_display = []
    # Pre-procesar nombres para la plantilla y evitar el filtro 'split'
    for ambiente in AMBIENTES_MAPA:
        ambientes_con_display.append({**ambiente, 'nombre_display': ambiente['nombre'].split('(')[0].strip()})

    context = {
        'posicion': posicion_gps,
        'ambientes': ambientes_con_display,
    }
    return render(request, 'usuarios/aprendiz/calificaciones.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_instructores_view(request):
    # TODO: Obtener los instructores asociados a la ficha del aprendiz
    instructores_ejemplo = [
        {'id': 1, 'nombre_completo': 'Ricardo Gómez', 'email': 'ricardo.gomez@sena.edu.co', 'especialidad': 'Instructor Técnico - Bases de Datos'},
        {'id': 2, 'nombre_completo': 'Laura Nuñez', 'email': 'laura.nunez@sena.edu.co', 'especialidad': 'Instructora Técnica - Desarrollo Web'},
        {'id': 3, 'nombre_completo': 'Sandra Milena', 'email': 'sandra.milena@sena.edu.co', 'especialidad': 'Instructora de Seguimiento y Ética'},
    ]
    context = {
        'instructores': instructores_ejemplo
    }
    return render(request, 'usuarios/aprendiz/instructores.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_instructor_detalle_view(request, instructor_id):
    # TODO: Obtener el instructor detallado desde la BD
    instructores_ejemplo = [
        {'id': 1, 'nombre_completo': 'Ricardo Gómez', 'email': 'ricardo.gomez@sena.edu.co', 'especialidad': 'Instructor Técnico - Bases de Datos', 'telefono': '3101234567', 'horario_atencion': 'Lunes a Viernes 8:00 - 12:00', 'materias': ['Bases de Datos', 'SQL', 'Modelado de Datos']},
        {'id': 2, 'nombre_completo': 'Laura Nuñez', 'email': 'laura.nunez@sena.edu.co', 'especialidad': 'Instructora Técnica - Desarrollo Web', 'telefono': '3119876543', 'horario_atencion': 'Lunes a Viernes 13:00 - 17:00', 'materias': ['HTML', 'CSS', 'JavaScript', 'React']},
        {'id': 3, 'nombre_completo': 'Sandra Milena', 'email': 'sandra.milena@sena.edu.co', 'especialidad': 'Instructora de Seguimiento y Ética', 'telefono': '3125558899', 'horario_atencion': 'Martes y Jueves 10:00 - 14:00', 'materias': ['Ética Profesional', 'Seguimiento Académico']},
    ]
    instructor = next((i for i in instructores_ejemplo if i['id'] == instructor_id), None)
    if not instructor:
        # TODO: Manejar instructor no encontrado
        pass
    context = {
        'instructor': instructor
    }
    return render(request, 'usuarios/aprendiz/instructor_detalle.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_cursos_view(request):
    # TODO: Obtener los cursos complementarios del aprendiz
    cursos_ejemplo = [
        {'nombre': 'Inglés para Desarrollo de Software Nivel 1', 'estado': 'En curso', 'progreso': 60},
        {'nombre': 'Manejo de Adobe Photoshop', 'estado': 'Completado', 'progreso': 100},
        {'nombre': 'Fundamentos de Ciberseguridad', 'estado': 'Inscrito', 'progreso': 0},
    ]
    context = {'cursos': cursos_ejemplo}
    return render(request, 'usuarios/aprendiz/cursos.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_curso_detalle_view(request, curso_id):
    # TODO: Obtener el curso detallado desde la BD
    cursos_ejemplo = [
        {'id': 1, 'nombre': 'Inglés para Desarrollo de Software Nivel 1', 'estado': 'En curso', 'progreso': 60, 'descripcion': 'Curso básico de inglés técnico para desarrolladores de software, enfocado en vocabulario específico de la industria.', 'instructor': 'Laura Nuñez', 'horario': 'Lunes y Miércoles 14:00 - 16:00', 'duracion': '40 horas', 'requisitos': 'Ninguno', 'objetivos': ['Mejorar el vocabulario técnico en inglés', 'Comprender documentación en inglés', 'Comunicarse efectivamente en entornos internacionales']},
        {'id': 2, 'nombre': 'Manejo de Adobe Photoshop', 'estado': 'Completado', 'progreso': 100, 'descripcion': 'Curso práctico para aprender a usar Adobe Photoshop en diseño gráfico y edición de imágenes.', 'instructor': 'Ricardo Gómez', 'horario': 'Martes y Jueves 10:00 - 12:00', 'duracion': '30 horas', 'requisitos': 'Conocimientos básicos de computación', 'objetivos': ['Dominar herramientas de edición de imágenes', 'Crear diseños gráficos profesionales', 'Aplicar técnicas de retoque fotográfico']},
        {'id': 3, 'nombre': 'Fundamentos de Ciberseguridad', 'estado': 'Inscrito', 'progreso': 0, 'descripcion': 'Introducción a los conceptos básicos de ciberseguridad, amenazas y mejores prácticas para proteger sistemas e información.', 'instructor': 'Sandra Milena', 'horario': 'Viernes 9:00 - 13:00', 'duracion': '50 horas', 'requisitos': 'Ninguno', 'objetivos': ['Entender conceptos de ciberseguridad', 'Identificar amenazas comunes', 'Aplicar medidas de protección básica']},
    ]
    curso = next((c for c in cursos_ejemplo if c['id'] == curso_id), None)
    if not curso:
        # TODO: Manejar curso no encontrado
        pass
    context = {
        'curso': curso
    }
    return render(request, 'usuarios/aprendiz/curso_detalle.html', context)

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_noticias_view(request):
    return render(request, 'usuarios/aprendiz/noticias.html')

@login_required
@role_required(allowed_roles=['aprendiz'])
def aprendiz_soporte_view(request):
    # TODO: Obtener anuncios reales desde la BD
    anuncios_ejemplo = [
        {'titulo': 'Cambio en el horario de clases', 'fecha': '2024-10-01', 'contenido': 'Se informa que a partir de la próxima semana, las clases de Desarrollo Front-End se trasladarán al Ambiente 302.'},
        {'titulo': 'Convocatoria a taller de ciberseguridad', 'fecha': '2024-09-28', 'contenido': 'El próximo viernes se realizará un taller gratuito sobre fundamentos de ciberseguridad. Inscripciones abiertas hasta el jueves.'},
        {'titulo': 'Felicitaciones por el desempeño', 'fecha': '2024-09-25', 'contenido': 'Felicitamos a los aprendices de la ficha 2556678 por su excelente participación en el proyecto de Bases de Datos.'},
    ]
    context = {'anuncios': anuncios_ejemplo}
    return render(request, 'usuarios/aprendiz/soporte.html', context)


# --- Vistas para el Panel del Admin ---
@login_required
@role_required(allowed_roles=['administrativo'])
def admin_usuarios_view(request):
    # Obtenemos todos los usuarios excepto el superusuario para no mostrarlo en la lista
    usuarios = Usuario.objects.filter(is_superuser=False).order_by('first_name', 'last_name', 'username')
    context = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/admin/admin_usuarios.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_programas_view(request):
    programas = Programa.objects.all().order_by('nombre')
    context = {
        'programas': programas
    }
    return render(request, 'usuarios/admin/admin_programas.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_fichas_view(request):
    nivel_filtro = request.GET.get('nivel')
    
    fichas_qs = Ficha.objects.select_related('programa').all()

    if nivel_filtro and nivel_filtro != 'todos':
        fichas_qs = fichas_qs.filter(programa__nivel=nivel_filtro)

    # Obtenemos los niveles disponibles para los botones de filtro
    niveles_disponibles = Programa.objects.values_list('nivel', flat=True).distinct()

    context = {
        'fichas': fichas_qs,
        'niveles': [n for n in niveles_disponibles if n], # Filtramos nulos o vacíos
        'filtro_actual': nivel_filtro
    }
    return render(request, 'usuarios/admin/admin_fichas.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_ficha_crear_view(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ficha creada exitosamente.')
            return redirect('admin_fichas')
    else:
        form = FichaForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nueva Ficha'
    }
    return render(request, 'usuarios/admin/admin_ficha_form.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_ficha_gestionar_aprendices_view(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id)
    
    # Aprendices que ya están en esta ficha
    aprendices_en_ficha = Usuario.objects.filter(rol='aprendiz', ficha=ficha).order_by('last_name', 'first_name')
    
    # Aprendices que no tienen ninguna ficha asignada
    aprendices_disponibles = Usuario.objects.filter(rol='aprendiz', ficha__isnull=True).order_by('last_name', 'first_name')
    
    context = {
        'ficha': ficha,
        'aprendices_en_ficha': aprendices_en_ficha,
        'aprendices_disponibles': aprendices_disponibles,
    }
    return render(request, 'usuarios/admin/admin_ficha_gestionar_aprendices.html', context)

@require_POST
@login_required
@role_required(allowed_roles=['administrativo'])
def admin_ficha_agregar_aprendiz_view(request, ficha_id, usuario_id):
    ficha = get_object_or_404(Ficha, id=ficha_id)
    
    # Verificamos si la ficha ya está llena
    if ficha.aprendices.count() >= ficha.cupo_maximo:
        messages.error(request, f"No se puede agregar al aprendiz. La ficha #{ficha.numero} ya ha alcanzado su cupo máximo de {ficha.cupo_maximo} personas.")
    else:
        aprendiz = get_object_or_404(Usuario, id=usuario_id, rol='aprendiz')
        aprendiz.ficha = ficha
        aprendiz.programa = ficha.programa # Asignamos también el programa de la ficha
        aprendiz.save()
        messages.success(request, f"'{aprendiz.get_full_name()}' ha sido añadido a la ficha #{ficha.numero}.")
    return redirect('admin_ficha_gestionar_aprendices', ficha_id=ficha.id)

@require_POST
@login_required
@role_required(allowed_roles=['administrativo'])
def admin_ficha_remover_aprendiz_view(request, ficha_id, usuario_id):
    aprendiz = get_object_or_404(Usuario, id=usuario_id, rol='aprendiz', ficha_id=ficha_id)
    aprendiz.ficha = None
    aprendiz.programa = None
    aprendiz.save()
    messages.success(request, f"'{aprendiz.get_full_name()}' ha sido removido de la ficha.")
    return redirect('admin_ficha_gestionar_aprendices', ficha_id=ficha_id)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_ficha_eliminar_view(request, ficha_id):
    ficha = Ficha.objects.get(id=ficha_id)
    if request.method == 'POST':
        ficha.delete()
        messages.success(request, f"Ficha #{ficha.numero} eliminada correctamente.")
        return redirect('admin_fichas')
    
    # Si no es POST, puedes mostrar una página de confirmación (opcional)
    return redirect('admin_fichas')

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_programa_crear_view(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Programa creado exitosamente.')
            return redirect('admin_programas')
    else:
        form = ProgramaForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Programa'
    }
    return render(request, 'usuarios/admin/admin_programa_form.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_programa_eliminar_view(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    if request.method == 'POST':
        programa.delete()
        messages.success(request, f"Programa '{programa.nombre}' eliminado correctamente.")
        return redirect('admin_programas')
    
    return redirect('admin_programas')

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_usuario_crear_view(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('admin_usuarios')
    else:
        form = UsuarioCreationForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Usuario'
    }
    return render(request, 'usuarios/admin/admin_usuario_form.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_usuario_eliminar_view(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        # No permitimos eliminar al usuario que está logueado
        if request.user.id != usuario.id:
            usuario.delete()
            messages.success(request, f"Usuario '{usuario.username}' eliminado correctamente.")
    return redirect('admin_usuarios')

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_reportes_view(request):
    # TODO: Obtener datos reales para los reportes
    context = {
        'total_usuarios': 150,
        'total_aprendices': 120,
        'total_instructores': 25,
        'total_administrativos': 5,
        'total_fichas': 10,
        'total_programas': 4,
    }
    return render(request, 'usuarios/admin/admin_reportes.html', context)

# --- Vistas de Edición para el Panel del Admin ---

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_usuario_editar_view(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = UsuarioAdminForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, f"Usuario '{usuario.username}' actualizado correctamente.")
            return redirect('admin_usuarios')
    else:
        form = UsuarioAdminForm(instance=usuario)

    context = {
        'form': form,
        'titulo': f'Editar Usuario: {usuario.username}'
    }
    return render(request, 'usuarios/admin/admin_usuario_form.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_programa_editar_view(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            messages.success(request, f"Programa '{programa.nombre}' actualizado correctamente.")
            return redirect('admin_programas')
    else:
        form = ProgramaForm(instance=programa)

    context = {
        'form': form,
        'titulo': f"Editar Programa: {programa.nombre}"
    }
    return render(request, 'usuarios/admin/admin_programa_form.html', context)

@login_required
@role_required(allowed_roles=['administrativo'])
def admin_ficha_editar_view(request, ficha_id):
    ficha = Ficha.objects.get(id=ficha_id)
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            messages.success(request, f"Ficha #{ficha.numero} actualizada correctamente.")
            return redirect('admin_fichas')
    else:
        form = FichaForm(instance=ficha)

    context = {
        'form': form,
        'titulo': f'Editar Ficha #{ficha.numero}'
    }
    return render(request, 'usuarios/admin/admin_ficha_form.html', context)


# --- Vistas para el Panel del Instructor ---
@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_fichas_view(request):
    # TODO: Reemplazar con la lógica real para obtener las fichas del instructor
    fichas_ejemplo = [
        {'id': 1, 'numero': '2556678', 'programa': 'Análisis y Desarrollo de Software'},
        {'id': 2, 'numero': '2558341', 'programa': 'Producción Multimedia', 'jornada': 'Diurna', 'aprendices_count': 25},
    ]
    context = {
        'fichas': fichas_ejemplo
    }
    return render(request, 'usuarios/instructor/instructor_fichas.html', context)

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_ubicacion_view(request):
    """
    Vista para mostrar la ubicación simulada del instructor en un plano.
    """
    # Coordenadas GPS de prueba (porcentaje de la pantalla)
    # En un caso real, esto vendría de un API o un dispositivo.
    posicion_gps = {'x': 70, 'y': 85}  # Ejemplo: 70% desde la izquierda, 85% desde arriba

    ambientes_con_display = []

    # Pre-procesar nombres para la plantilla y evitar el filtro 'split'
    for ambiente in AMBIENTES_MAPA:
        ambientes_con_display.append({**ambiente, 'nombre_display': ambiente['nombre'].split('(')[0].strip()})

    context = {
        'posicion': posicion_gps,
        'ambientes': ambientes_con_display,
    }
    return render(request, 'usuarios/instructor/instructor_ubicacion.html', context)

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_horarios_view(request):
    # TODO: Reemplazar con la lógica real para obtener los horarios del instructor desde la BD
    horarios_ejemplo = [
        {'id': 1, 'ficha_numero': '2556678', 'programa': 'Análisis y Desarrollo de Software', 'competencia': 'Diseño de Interfaces', 'dia': 'Lunes', 'hora_inicio': '08:00', 'hora_fin': '12:00', 'ambiente': 'Ambiente 301'},
        {'id': 2, 'ficha_numero': '2558341', 'programa': 'Producción Multimedia', 'competencia': 'Modelado 3D', 'dia': 'Martes', 'hora_inicio': '14:00', 'hora_fin': '18:00', 'ambiente': 'Ambiente 205'},
        {'id': 3, 'ficha_numero': '2556678', 'programa': 'Análisis y Desarrollo de Software', 'competencia': 'Bases de Datos', 'dia': 'Miércoles', 'hora_inicio': '10:00', 'hora_fin': '14:00', 'ambiente': 'Ambiente 301'},
        {'id': 4, 'ficha_numero': '2558341', 'programa': 'Producción Multimedia', 'competencia': 'Edición de Video', 'dia': 'Jueves', 'hora_inicio': '08:00', 'hora_fin': '12:00', 'ambiente': 'Estudio de Grabación'},
        {'id': 5, 'ficha_numero': '2556678', 'programa': 'Análisis y Desarrollo de Software', 'competencia': 'Desarrollo Front-End', 'dia': 'Lunes', 'hora_inicio': '13:00', 'hora_fin': '17:00', 'ambiente': 'Ambiente 302'},
    ]

    # Agrupar horarios por día para la vista de calendario
    horarios_por_dia = {}
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    for dia in dias_semana:
        horarios_por_dia[dia] = sorted(
            [h for h in horarios_ejemplo if h['dia'] == dia], 
            key=lambda x: x['hora_inicio']
        )

    context = {
        'horarios_por_dia': horarios_por_dia
    }

    return render(request, 'usuarios/instructor/instructor_horarios.html', context)

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_anuncios_view(request):
    return render(request, 'usuarios/instructor/instructor_anuncios.html')

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_reportes_view(request):
    if request.method == 'POST':
        # TODO: Procesar el formulario para crear un nuevo reporte
        messages.success(request, 'Reporte creado exitosamente.')
        return redirect('instructor_reportes')

    # TODO: Obtener reportes reales desde la base de datos
    reportes_ejemplo = [
        {'tipo': 'Sanción', 'aprendiz': 'Carlos Alberto Pérez', 'ficha': '2556678', 'fecha': '2024-05-10', 'descripcion': 'Llamado de atención verbal por inasistencia.'},
        {'tipo': 'Deserción', 'aprendiz': 'Laura Sofía Cadena', 'ficha': '2558341', 'fecha': '2024-04-22', 'descripcion': 'Aprendiz no ha asistido por más de 3 días sin justificación.'},
        {'tipo': 'Felicitación', 'aprendiz': 'Ana María López', 'ficha': '2556678', 'fecha': '2024-05-15', 'descripcion': 'Excelente desempeño en la competencia de Diseño de Interfaces.'},
        {'tipo': 'Sanción', 'aprendiz': 'Juan David Restrepo', 'ficha': '2556678', 'fecha': '2024-03-18', 'descripcion': 'Llamado de atención escrito por uso inadecuado de equipos.'},
    ]
    # Asignar IDs a los reportes para enlaces
    for i, reporte in enumerate(reportes_ejemplo):
        reporte['id'] = i + 1

    tipos_reporte = sorted(list(set(r['tipo'] for r in reportes_ejemplo)))

    # TODO: Obtener fichas reales del instructor
    fichas_ejemplo = [
        {'id': 1, 'numero': '2556678', 'programa': 'Análisis y Desarrollo de Software'},
        {'id': 2, 'numero': '2558341', 'programa': 'Producción Multimedia'},
    ]

    # TODO: Obtener aprendices reales
    aprendices_ejemplo = [
        {'id': 101, 'ficha_id': 1, 'nombre_completo': 'Ana María López'},
        {'id': 102, 'ficha_id': 1, 'nombre_completo': 'Carlos Alberto Pérez'},
        {'id': 103, 'ficha_id': 1, 'nombre_completo': 'Sofía Rodríguez Gómez'},
        {'id': 104, 'ficha_id': 2, 'nombre_completo': 'Laura Sofía Cadena'},
        {'id': 105, 'ficha_id': 2, 'nombre_completo': 'Juan David Restrepo'},
    ]

    context = {
        'reportes': reportes_ejemplo,
        'tipos_reporte': tipos_reporte,
        'fichas': fichas_ejemplo,
        'aprendices': aprendices_ejemplo
    }
    return render(request, 'usuarios/instructor/instructor_reportes.html', context)

@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_reporte_detalle_view(request, reporte_id):
    # TODO: Reemplazar con la lógica real para obtener el reporte desde la BD
    reportes_ejemplo = [
        {'id': 1, 'tipo': 'Sanción', 'aprendiz': 'Carlos Alberto Pérez', 'ficha': '2556678', 'fecha': '2024-05-10', 'descripcion': 'Llamado de atención verbal por inasistencia.', 'gravedad': 'Leve', 'acciones': 'Se realiza seguimiento semanal.'},
        {'id': 2, 'tipo': 'Deserción', 'aprendiz': 'Laura Sofía Cadena', 'ficha': '2558341', 'fecha': '2024-04-22', 'descripcion': 'Aprendiz no ha asistido por más de 3 días sin justificación.', 'gravedad': 'Grave', 'acciones': 'Se inicia proceso de deserción según reglamento.'},
        {'id': 3, 'tipo': 'Felicitación', 'aprendiz': 'Ana María López', 'ficha': '2556678', 'fecha': '2024-05-15', 'descripcion': 'Excelente desempeño en la competencia de Diseño de Interfaces.', 'gravedad': 'N/A', 'acciones': 'Se anota en el historial académico.'},
        {'id': 4, 'tipo': 'Sanción', 'aprendiz': 'Juan David Restrepo', 'ficha': '2556678', 'fecha': '2024-03-18', 'descripcion': 'Llamado de atención escrito por uso inadecuado de equipos.', 'gravedad': 'Moderada', 'acciones': 'Se suspende el acceso al equipo por una semana.'},
    ]
    # Asignamos un 'id' a cada reporte para poder buscarlo
    for i, reporte in enumerate(reportes_ejemplo):
        reporte['id'] = i + 1

    reporte_seleccionado = next((r for r in reportes_ejemplo if r['id'] == reporte_id), None)

    context = {
        'reporte': reporte_seleccionado
    }
    # Asegúrate de tener una plantilla en 'usuarios/instructor/instructor_reporte_detalle.html'
    return render(request, 'usuarios/instructor/instructor_reporte_detalle.html', context)


@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_ficha_aprendices_view(request, ficha_id):
    # TODO: Reemplazar con la lógica real para obtener la ficha y sus aprendices
    # ficha = get_object_or_404(Ficha, id=ficha_id)
    # aprendices = Usuario.objects.filter(ficha=ficha, rol='aprendiz')

    # Datos de ejemplo para la demostración
    fichas_db = {1: {'id': 1, 'numero': '2556678', 'programa': 'Análisis y Desarrollo de Software'}, 2: {'id': 2, 'numero': '2558341', 'programa': 'Producción Multimedia'}}
    ficha_ejemplo = fichas_db.get(ficha_id, {'id': ficha_id, 'numero': 'Desconocida', 'programa': ''})
    aprendices_ejemplo = [
        {'id': 101, 'nombre_completo': 'Ana María López', 'documento': '1029384756'},
        {'id': 102, 'nombre_completo': 'Carlos Alberto Pérez', 'documento': '1098765432'},
        {'id': 103, 'nombre_completo': 'Sofía Rodríguez Gómez', 'documento': '1012345678'},
    ]

    context = {
        'ficha': ficha_ejemplo,
        'aprendices': aprendices_ejemplo
    }
    return render(request, 'usuarios/instructor/instructor_ficha_aprendices.html', context)


@login_required
@role_required(allowed_roles=['instructor', 'administrativo'])
def instructor_aprendiz_perfil_view(request, ficha_id, aprendiz_id):
    # --- Base de datos de ejemplo ---
    # TODO: Reemplazar con la lógica real de la base de datos
    fichas_db = {
        1: {'id': 1, 'numero': '2556678', 'programa': 'Análisis y Desarrollo de Software'}, 
        2: {'id': 2, 'numero': '2558341', 'programa': 'Producción Multimedia'}
    }
    aprendices_db = {
        101: {'id': 101, 'nombre_completo': 'Ana María López', 'documento': '1029384756', 'email': 'ana.lopez@example.com', 'telefono': '3101234567'},
        102: {'id': 102, 'nombre_completo': 'Carlos Alberto Pérez', 'documento': '1098765432', 'email': 'carlos.perez@example.com', 'telefono': '3119876543'},
        103: {'id': 103, 'nombre_completo': 'Sofía Rodríguez Gómez', 'documento': '1012345678', 'email': 'sofia.rodriguez@example.com', 'telefono': '3125558899'},
    }
    calificaciones_db = {
        101: [
            {'competencia': 'Diseño de Interfaces', 'resultado': 'A', 'juicio': 'Aprobado'},
            {'competencia': 'Desarrollo Front-End', 'resultado': 'A', 'juicio': 'Aprobado'},
            {'competencia': 'Bases de Datos', 'resultado': 'D', 'juicio': 'Por evaluar'},
        ],
        102: [
            {'competencia': 'Diseño de Interfaces', 'resultado': 'A', 'juicio': 'Aprobado'},
            {'competencia': 'Desarrollo Front-End', 'resultado': 'D', 'juicio': 'Por evaluar'},
        ]
    }
    # --- Fin de la base de datos de ejemplo ---

    ficha_ejemplo = fichas_db.get(ficha_id)
    aprendiz_ejemplo = aprendices_db.get(aprendiz_id)
    calificaciones_ejemplo = calificaciones_db.get(aprendiz_id, [])

    if request.method == 'POST':
        competencia = request.POST.get('competencia')
        resultado = request.POST.get('resultado')
        juicio = 'Aprobado' if resultado == 'A' else 'Por evaluar'
        
        # Lógica para guardar la calificación (aquí solo se simula)
        # En un caso real, se crearía o actualizaría un registro en la BD.
        calificaciones_db.setdefault(aprendiz_id, []).append({
            'competencia': competencia,
            'resultado': resultado,
            'juicio': juicio
        })
        messages.success(request, f"Se ha registrado la calificación para {competencia}.")
        return redirect('instructor_aprendiz_perfil', ficha_id=ficha_id, aprendiz_id=aprendiz_id)

    # TODO: Añadir un 404 si no se encuentra el aprendiz
    competencias_programa = [
        'Diseñar la solución de software', 'Construir el software', 'Realizar pruebas al software', 'Implantar la solución de software', 'Promover la interacción idónea'
    ]

    context = {
        'ficha': ficha_ejemplo,
        'aprendiz': aprendiz_ejemplo,
        'calificaciones': calificaciones_ejemplo,
        'competencias_programa': competencias_programa,
    }
    return render(request, 'usuarios/instructor/instructor_aprendiz_perfil.html', context)
