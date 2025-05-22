from django.db import models
from .endereco import Endereco

class Associacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'associação'
        verbose_name_plural = 'associações'
