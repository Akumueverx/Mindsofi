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






from django.db import models


class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    contraseña = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nombre_completo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'registro'


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Registrorol(models.Model):
    id = models.AutoField(primary_key=True)
    idregistro = models.ForeignKey(Registro, models.CASCADE, db_column='idregistro')
    idrol = models.ForeignKey(Rol, models.CASCADE, db_column='idRol')

    class Meta:
        managed = False
        db_table = 'registroRol'


class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20)
    duracion = models.CharField(max_length=20)
    etapa = models.CharField(max_length=20)
    idespecialidad = models.ForeignKey(Especialidad, models.CASCADE, db_column='idespecialidad')

    class Meta:
        managed = False
        db_table = 'programa'


class Ficha(models.Model):
    id = models.AutoField(primary_key=True)
    numero_ficha = models.IntegerField(unique=True)
    jornada = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ficha'


class Programaficha(models.Model):
    id = models.AutoField(primary_key=True)
    idprograma = models.ForeignKey(Programa, models.CASCADE, db_column='idprograma')
    idficha = models.ForeignKey(Ficha, models.CASCADE, db_column='idFicha')

    class Meta:
        managed = False
        db_table = 'programaFicha'


class Instructorespecialidad(models.Model):
    id = models.AutoField(primary_key=True)
    idregistrorol = models.ForeignKey(Registrorol, models.CASCADE, db_column='idregistroRol')
    idespecialidad = models.ForeignKey(Especialidad, models.CASCADE, db_column='idespecialidad')

    class Meta:
        managed = False
        db_table = 'instructor_especialidad'


class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    intensidad_horaria = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'asignatura'


class Especialidadasignatura(models.Model):
    id = models.AutoField(primary_key=True)
    idespecialidad = models.ForeignKey(Instructorespecialidad, models.CASCADE, db_column='idespecialidad')
    idasignatura = models.ForeignKey(Asignatura, models.CASCADE, db_column='idAsignatura')

    class Meta:
        managed = False
        db_table = 'especialidadAsignatura'


class Salon(models.Model):
    id = models.AutoField(primary_key=True)
    numero_salon = models.CharField(unique=True, max_length=20)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salon'


class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    idasignatura = models.ForeignKey(Asignatura, models.CASCADE, db_column='idAsignatura')
    idinstructor_especialidad = models.ForeignKey(Instructorespecialidad, models.CASCADE, db_column='idinstructor_especialidad')
    idficha = models.ForeignKey(Ficha, models.CASCADE, db_column='idFicha')
    idsalon = models.ForeignKey(Salon, models.CASCADE, db_column='idSalon', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clase'


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    idclase = models.ForeignKey(Clase, models.CASCADE, db_column='idclase')
    idsalon = models.ForeignKey(Salon, models.CASCADE, db_column='idSalon')

    class Meta:
        managed = False
        db_table = 'horario'

