from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.

class Familiares(models.Model):

    edad = models.IntegerField()
    nombre= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
