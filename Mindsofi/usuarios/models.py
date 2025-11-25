from django.contrib.auth.models import AbstractUser
from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nivel = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Ficha(models.Model):
    JORNADA_CHOICES = [('Diurna', 'Diurna'), ('Nocturna', 'Nocturna'), ('Mixta', 'Mixta'), ('Fines de semana', 'Fines de semana')]
    numero = models.CharField(max_length=20, unique=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='fichas')
    jornada = models.CharField(max_length=20, choices=JORNADA_CHOICES, default='Diurna')
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    cupo_maximo = models.PositiveIntegerField(default=30, help_text="Número máximo de aprendices en la ficha.")

    def __str__(self):
        return f"{self.numero} - {self.programa.nombre}"

class Reporte(models.Model):
    TIPO_REPORTE_CHOICES = [
        ('Felicitación', 'Felicitación'),
        ('Llamado de atención verbal', 'Llamado de atención verbal'),
        ('Llamado de atención escrito', 'Llamado de atención escrito'),
        ('Sanción', 'Sanción'),
        ('Deserción', 'Deserción'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_REPORTE_CHOICES)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprendiz = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='reportes_recibidos', limit_choices_to={'rol': 'aprendiz'})
    instructor = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, related_name='reportes_creados', limit_choices_to={'rol': 'instructor'})
    ficha = models.ForeignKey(Ficha, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reporte de {self.tipo} para {self.aprendiz.username} el {self.fecha_creacion.strftime('%Y-%m-%d')}"

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('aprendiz', 'Aprendiz'),
        ('instructor', 'Instructor'),
        ('administrativo', 'Administrativo'),
    ]
    GENERO_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]

    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='aprendiz')
    # Campos para Aprendiz
    programa = models.ForeignKey(
        Programa,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    ficha = models.ForeignKey(
        Ficha,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='aprendices'
    )
    # Campos generales
    documento = models.CharField(max_length=30, blank=True, null=True, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, blank=True, null=True)
    # Campo para Instructor
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    # Campo para Administrativo
    cargo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
