from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    
    # URLs del panel de administración
    path('dashboard/', views.dashboard_admin_view, name='dashboard_admin'),
    
    # URLs de ejemplo para las demás secciones del admin
    path('admin/usuarios/', views.dashboard_admin_view, name='admin_usuarios'),
    path('admin/programas/', views.dashboard_admin_view, name='admin_programas'),
    path('admin/fichas/', views.dashboard_admin_view, name='admin_fichas'),
    path('admin/reportes/', views.dashboard_admin_view, name='admin_reportes'),
]