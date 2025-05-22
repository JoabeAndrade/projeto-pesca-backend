from django.db import models
from .municipio import Municipio

class Comunidade(models.Model):
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='comunidades')
