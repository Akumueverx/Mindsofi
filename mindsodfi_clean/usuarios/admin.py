from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol y Datos', {'fields': ('rol', 'programa', 'ficha', 'documento', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol y Datos', {'fields': ('rol', 'programa', 'ficha', 'documento', 'telefono')}),
    )
