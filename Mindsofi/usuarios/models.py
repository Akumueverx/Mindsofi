from django.contrib.auth.models import AbstractUser
from django.db import models

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
    PROGRAMA_CHOICES = [
        ('', 'Seleccione un programa'),
        ('programacion', 'Programación de Software'),
        ('electricidad', 'Electricidad Industrial'),
        ('telecomunicaciones', 'Telecomunicaciones'),
        ('audiovisual', 'Producción Audiovisual'),
        ('mantenimiento', 'Mantenimiento Electromecánico'),
        ('diseno_grafico', 'Diseño Gráfico'),
        ('contabilidad', 'Contabilidad y Finanzas'),
    ]
    FICHA_CHOICES = [
        ('', 'Seleccione una ficha'),
        ('2556678', '2556678'), ('3175010', '3175010'), ('2003120', '2003120'),
        ('2558341', '2558341'), ('2559123', '2559123'), ('2670689', '2670689'),
        ('2694501', '2694501'), ('2712345', '2712345'), ('2722890', '2722890'),
        ('2735678', '2735678'), ('2748901', '2748901'), ('2754321', '2754321'),
        ('2769876', '2769876'), ('2781122', '2781122'), ('2793344', '2793344'),
        ('2805566', '2805566'), ('2817788', '2817788'), ('2829900', '2829900'),
        ('2831234', '2831234'), ('2845678', '2845678'),
    ]

    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='aprendiz')
    # Campos para Aprendiz
    programa = models.CharField(
        max_length=100,
        choices=PROGRAMA_CHOICES,
        blank=True,
        null=True
    )
    ficha = models.CharField(
        max_length=30,
        choices=FICHA_CHOICES,
        blank=True,
        null=True
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
