from django.db import models
from .municipio import Municipio

class Comunidade(models.Model):
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='comunidades')

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome
