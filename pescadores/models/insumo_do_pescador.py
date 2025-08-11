from django.db import models
from django.core.validators import MinValueValidator

from .tipo_insumo import TipoInsumo
from .pescador_especialista import PescadorEspecialista

from decimal import Decimal

class InsumoDoPescador(models.Model):
    tipo = models.ForeignKey(TipoInsumo, on_delete=models.PROTECT)
    valor = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0))],
        blank=True,
        null=True,
    )
    pescador_especialista = models.ForeignKey(
        PescadorEspecialista,
        on_delete=models.CASCADE,
        related_name='insumos',
    )

    class Meta:
        unique_together = ['tipo', 'pescador_especialista']
        verbose_name = 'insumo'
        verbose_name_plural = 'insumos'
