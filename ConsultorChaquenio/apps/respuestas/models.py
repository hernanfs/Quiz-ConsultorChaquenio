from django.db import models
from apps.preguntas.models import Pregunta
# Create your models here.

class Respuesta(models.Model):
	pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
	respuestas = models.TextField(verbose_name='Escriba su respuesta:')
	respuesta_correcta = models.BooleanField(verbose_name='Marca esta casilla cuando cargues la respuesta correcta.', default=False, null=False);

	def __str__(self):
		return self.respuestas