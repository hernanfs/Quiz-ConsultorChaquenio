from django.db import models
from apps.categorias.models import Categoria

# Create your models here.

class Pregunta(models.Model):
	categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
	enunciado = models.TextField(verbose_name='Escriba su enunciado')

	def __str__(self):
		return self.enunciado