from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Espacio(models.Model):
    nombre_espacio = models.CharField(max_length=100)
    maximo_persona_espacio = models.IntegerField()
    tablero_espacio = models.BooleanField(default=False)
    videobeam_espacio = models.BooleanField(default=False)
    cantidad_sillas_espacio = models.IntegerField()
    conectividad_internet = models.BooleanField(default=False)
    dependencia = models.ForeignKey('Dependencia', on_delete=models.CASCADE)

class Reserva(models.Model):
    espacio = models.ForeignKey('Espacio', on_delete=models.CASCADE)
    usuario_reserva = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio_reserva = models.TimeField()
    hora_final_reserva = models.TimeField()
    externo = models.ForeignKey('UsuarioExterno', null=True, blank=True, on_delete=models.SET_NULL)

class UsuarioExterno(models.Model):
    nit_cc_externo = models.CharField(max_length=20)
    nombre_usuario_externo = models.CharField(max_length=100)
    email_usuario_externo = models.EmailField()
    telefono_externo = models.CharField(max_length=20)
    responsable_usuario_externo = models.CharField(max_length=100)

class Dependencia(models.Model):
    nombre_dependencia = models.CharField(max_length=100)
    telefono_dependencia = models.CharField(max_length=20)
    correo_dependencia = models.EmailField()

class Horario(models.Model):
    espacio = models.ForeignKey('Espacio', on_delete=models.CASCADE)
    fecha_horario = models.DateField()
    hora_inicio_horario = models.TimeField()
    hora_final_horario = models.TimeField()
