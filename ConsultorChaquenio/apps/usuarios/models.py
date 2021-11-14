from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import *

class Usuario (AbstractUser):
	localidad = models.CharField(max_length=50, null=True);	

	puntaje_total = models.FloatField(default=0);