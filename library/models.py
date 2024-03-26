from django.db import models

# Create your models here.

class participantes(models.Model):
    id = models.AutoField(primary_key=True)
    sujeto = models.IntegerField()
    nombre = models.CharField(max_length=32)
    edad = models.IntegerField()
    cedula = models.IntegerField(20)
    genero = models.CharField(max_length=9)
    escolaridad = models.CharField(max_length=11)
    A_escolaridad = models.IntegerField(4)
    grupo = models.CharField(max_length=3)
    cod_participante = models.CharField(max_length=11)
    visita = models.CharField(max_length=6)
    tarea = models.CharField(max_length=6)
    fecha = models.CharField(max_length=10)
#     # Datos = models.CharField(max_length=50)
