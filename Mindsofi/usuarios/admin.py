from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Ficha, Programa, Reporte, Horario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol y Datos', {'fields': ('rol', 'programa', 'ficha', 'documento', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol y Datos', {'fields': ('rol', 'programa', 'ficha', 'documento', 'telefono')}),
    )
    # Añadimos search_fields para asegurar la compatibilidad con autocomplete
    search_fields = ('username', 'first_name', 'last_name', 'email', 'documento')

class HorarioInline(admin.TabularInline):
    model = Horario
    extra = 1 # Muestra un formulario vacío para añadir un nuevo horario.
    autocomplete_fields = ['instructor']
    fields = ('dia', 'hora_inicio', 'hora_fin', 'instructor', 'competencia', 'ambiente')

@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'programa', 'jornada', 'instructor')
    list_filter = ('programa', 'jornada', 'instructor')
    search_fields = ('numero', 'programa__nombre', 'instructor__username')
    autocomplete_fields = ['instructor', 'programa']
    inlines = [HorarioInline] # ¡Aquí está la magia!

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel')
    search_fields = ('nombre',) # Campo de búsqueda para el autocompletado

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('ficha', 'instructor', 'competencia', 'dia', 'hora_inicio', 'hora_fin', 'ambiente')
    list_filter = ('dia', 'instructor', 'ficha', 'ambiente')
    search_fields = ('competencia', 'ficha__numero', 'instructor__username')
    autocomplete_fields = ['ficha', 'instructor']

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'aprendiz', 'instructor', 'fecha_creacion')
    list_filter = ('tipo', 'fecha_creacion', 'instructor')
    search_fields = ('aprendiz__username', 'instructor__username', 'descripcion')
    autocomplete_fields = ['aprendiz', 'instructor', 'ficha']
