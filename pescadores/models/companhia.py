from django.db import models
from django.core.validators import MinValueValidator
from .pescador_especialista import PescadorEspecialista
from .relacao_companhia import RelacaoCompanhia

class Companhia(models.Model):
    relacao = models.ForeignKey(RelacaoCompanhia, on_delete=models.PROTECT)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    especialista = models.ForeignKey(
        PescadorEspecialista,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ['especialista', 'relacao']
