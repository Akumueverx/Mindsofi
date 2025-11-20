from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('aprendiz', 'Aprendiz'),
        ('instructor', 'Instructor'),
        ('administrativo', 'Administrativo'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='aprendiz')
    programa = models.CharField(max_length=100, blank=True, null=True)
    ficha = models.CharField(max_length=30, blank=True, null=True)
    documento = models.CharField(max_length=30, blank=True, null=True, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


#--Modelos para Admin --

class Programa(models.Model):
    NIVELES = [
        ('tecnologo', 'Tecnólogo'),
        ('tecnico', 'Técnico'),
    ]
    
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, unique=True)
    nivel = models.CharField(max_length=20, choices=NIVELES)
    duracion_meses = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
