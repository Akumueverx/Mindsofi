from django.urls import path
from django.shortcuts import redirect, HttpResponse
from . import views

urlpatterns = [
    path("", lambda request: redirect("login"), name="home"),  # 👈 redirige al login
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("redirect/", views.redirect_dashboard, name="redirect_dashboard"),

    # Dashboards
    path("aprendiz/dashboard/", views.dashboard_aprendiz, name="dashboard_aprendiz"),
    path("instructor/dashboard/", views.dashboard_instructor, name="dashboard_instructor"),
    path("dashboard/admin/", views.dashboard_admin, name="dashboard_admin"),

    # URLs para los enlaces del dashboard de Aprendiz (placeholders por ahora)
    path("aprendiz/programa/", views.aprendiz_programa_view, name="programa_aprendiz"),
    path("aprendiz/ficha/", views.aprendiz_ficha_view, name="ficha_aprendiz"),
    path("aprendiz/ficha/detalle/", views.aprendiz_ficha_detalle_view, name="ficha_detalle_aprendiz"),
    path("aprendiz/horario/", views.aprendiz_horario_view, name="horario_aprendiz"),
    path("aprendiz/ubicacion/", views.aprendiz_ubicacion_view, name="ubicacion_aprendiz"),
    path("aprendiz/instructores/", views.aprendiz_instructores_view, name="instructores_aprendiz"),
    path("aprendiz/instructores/<int:instructor_id>/detalle/", views.aprendiz_instructor_detalle_view, name="instructor_detalle_aprendiz"),
    path("aprendiz/cursos/", views.aprendiz_cursos_view, name="cursos_aprendiz"),
    path("aprendiz/cursos/<int:curso_id>/detalle/", views.aprendiz_curso_detalle_view, name="curso_detalle_aprendiz"),
    path("aprendiz/noticias/", views.aprendiz_noticias_view, name="noticias_aprendiz"),
    path("aprendiz/soporte/", views.aprendiz_soporte_view, name="soporte_aprendiz"),

    # URLs para los enlaces del dashboard de Instructor (placeholders por ahora)
    path("instructor/fichas/", views.instructor_fichas_view, name="instructor_fichas"),
    path("instructor/ubicacion/", views.instructor_ubicacion_view, name="instructor_ubicacion"),
    path("instructor/horarios/", views.instructor_horarios_view, name="instructor_horarios"),
    path("instructor/anuncios/", views.instructor_anuncios_view, name="instructor_anuncios"),
    path("instructor/reportes/", views.instructor_reportes_view, name="instructor_reportes"),
    path("instructor/reportes/crear/", views.instructor_reporte_crear_view, name="instructor_reporte_crear"),
    path("instructor/reportes/<int:reporte_id>/", views.instructor_reporte_detalle_view, name="instructor_reporte_detalle"),
    path("instructor/fichas/<int:ficha_id>/aprendices/", views.instructor_ficha_aprendices_view, name="instructor_ficha_aprendices"),
    path("instructor/fichas/<int:ficha_id>/aprendices/<int:aprendiz_id>/", views.instructor_aprendiz_perfil_view, name="instructor_aprendiz_perfil"),

    # URLs para los enlaces del dashboard de Admin
    path("dashboard/admin/usuarios/", views.admin_usuarios_view, name="admin_usuarios"),
    path("dashboard/admin/programas/", views.admin_programas_view, name="admin_programas"),
    path("dashboard/admin/fichas/", views.admin_fichas_view, name="admin_fichas"),
    path("dashboard/admin/fichas/crear/", views.admin_ficha_crear_view, name="admin_ficha_crear"),
    path("dashboard/admin/usuarios/crear/", views.admin_usuario_crear_view, name="admin_usuario_crear"),
    path("dashboard/admin/programas/crear/", views.admin_programa_crear_view, name="admin_programa_crear"),
    path("dashboard/admin/reportes/", views.admin_reportes_view, name="admin_reportes"),
    # URLs para gestión de reportes por el Admin
    path("dashboard/admin/gestion-reportes/", views.admin_gestion_reportes_view, name="admin_gestion_reportes"),
    path("dashboard/admin/gestion-reportes/crear/", views.admin_reporte_crear_view, name="admin_reporte_crear"),
    path("dashboard/admin/gestion-reportes/<int:reporte_id>/", views.admin_reporte_detalle_view, name="admin_reporte_detalle"),

    # URLs para edición en el panel de Admin
    path("dashboard/admin/usuarios/<int:usuario_id>/editar/", views.admin_usuario_editar_view, name="admin_usuario_editar"),
    path("dashboard/admin/usuarios/<int:usuario_id>/eliminar/", views.admin_usuario_eliminar_view, name="admin_usuario_eliminar"),
    path("dashboard/admin/programas/<int:programa_id>/editar/", views.admin_programa_editar_view, name="admin_programa_editar"),
    path("dashboard/admin/programas/<int:programa_id>/eliminar/", views.admin_programa_eliminar_view, name="admin_programa_eliminar"),
    path("dashboard/admin/fichas/<int:ficha_id>/editar/", views.admin_ficha_editar_view, name="admin_ficha_editar"),
    path("dashboard/admin/fichas/<int:ficha_id>/eliminar/", views.admin_ficha_eliminar_view, name="admin_ficha_eliminar"),
    path("dashboard/admin/fichas/<int:ficha_id>/gestionar-horarios/", views.admin_ficha_gestionar_horarios_view, name="admin_ficha_gestionar_horarios"),
    # URLs para gestionar aprendices en una ficha
    path("dashboard/admin/fichas/<int:ficha_id>/gestionar-aprendices/", views.admin_ficha_gestionar_aprendices_view, name="admin_ficha_gestionar_aprendices"),
    path("dashboard/admin/fichas/<int:ficha_id>/agregar-aprendiz/<int:usuario_id>/", views.admin_ficha_agregar_aprendiz_view, name="admin_ficha_agregar_aprendiz"),
    path("dashboard/admin/fichas/<int:ficha_id>/remover-aprendiz/<int:usuario_id>/", views.admin_ficha_remover_aprendiz_view, name="admin_ficha_remover_aprendiz"),

    # URL para la ubicación en el panel de Admin
    path("dashboard/admin/ubicacion/", views.admin_ubicacion_view, name="admin_ubicacion"),
    path("dashboard/aprendiz/ubicacion/", views.aprendiz_ubicacion_view, name="aprendiz_ubicacion"),
]

