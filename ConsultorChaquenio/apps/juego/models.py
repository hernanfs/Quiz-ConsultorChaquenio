from django.db import models
from django.http import HttpResponse

from apps.preguntas.models import Pregunta
from apps.usuarios.models import Usuario

import random

# Create your models here.

excluidas = [];

class Funcionamiento(models.Model):

	def obtenerPreguntas():

		global excluidas;

		bandera=False;
		if ( len(excluidas)==0 ):

			pregunta = random.choice(Pregunta.objects.all());
			
		else:

			pregunta = random.choice(Pregunta.objects.all());

			while (bandera!=True):
				banderaI=True;
				for e in excluidas:
					if (pregunta.id == e):
						pregunta = random.choice(Pregunta.objects.all());
						banderaI=False;
						break;
				if (banderaI==True):
					bandera=True;


		excluidas.append(pregunta.id);

		if (len(excluidas)>9):

			for i in range (len(excluidas)):
				excluidas.pop();

		return (pregunta);
