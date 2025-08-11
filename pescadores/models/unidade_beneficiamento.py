from django.db import models

class UnidadeBeneficiamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'unidade de beneficiamento'
        verbose_name_plural = 'unidades de beneficiamento'
