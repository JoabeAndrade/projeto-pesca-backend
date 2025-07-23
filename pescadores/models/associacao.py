from django.db import models
from .endereco import Endereco

class Associacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'associação'
        verbose_name_plural = 'associações'
