from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
	#opciones de rango
	NOOB = 'NB'
	ADMIN = 'AD'
	LAMMER = 'LM'
	TROLL = 'TL'
	MEDIUM = 'MD'
	EXPERT = 'EX'
	MASTER = 'MS'
	CREADOR = 'CR'
	#lista con las opciones para el modelo
	CHOICES = ((NOOB, 'Noob'),
		(ADMIN, 'Administrador'),
		(LAMMER, 'Lammer'),
		(TROLL, 'Troll'),
		(MEDIUM, 'Medio'),
		(EXPERT, 'Experto'),
		(MASTER, 'Maestro'),
		(CREADOR, 'Creador'),
		)
	#modelo del resto de cosas
	nombre = models.CharField(max_length=200, null=False)
	email =  models.EmailField(max_length=250, null=False)
	rango = models.CharField(max_length=2, choices=CHOICES, default=NOOB)
	fecha_cre = models.DateTimeField(default=timezone.now())
	penalizaciones = models.IntegerField(default=0)
	art_apro = models.IntegerField(default=0)
	art_rech = models.IntegerField(default=0)

#tabla de articulos (no es necesaria mucha explicacion je)
class Articulo(models.Model):
	#variables estado
	REVISION = 'RV'
	RECHAZADO = 'RJ'
	ACEPTADO = 'AC'
	#otra vez una lista con opciones
	STATE = ((REVISION, 'En revision'),
		(RECHAZADO, 'rechazado'),
		(ACEPTADO, 'Aceptado'),
		)
	creador = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200, null=False)
	cuerpo = models.TextField(null=False)
	estado = models.CharField(max_length=2, choices=STATE, default=REVISION )
	puntos = models.IntegerField(default=0)
	#lo de abajo queda comentado hasta que implemente los comentarios
	#comentarios = models.ForeignKey('')