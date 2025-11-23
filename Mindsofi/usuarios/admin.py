from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .models import *

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol y Datos', {'fields': ('rol', 'programa', 'ficha', 'documento', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol y Datos', {'fields': ('rol', 'programa', 'ficha', 'documento', 'telefono')}),
    )



admin.site.register(Registro)
admin.site.register(Rol)
admin.site.register(Registrorol)
admin.site.register(Especialidad)
admin.site.register(Programa)
admin.site.register(Ficha)
admin.site.register(Programaficha)
admin.site.register(Instructorespecialidad)
admin.site.register(Asignatura)
admin.site.register(Especialidadasignatura)
admin.site.register(Salon)
admin.site.register(Clase)
admin.site.register(Horario)

