from django.db import models
from django.core.validators import MinValueValidator

from .fonte_renda_durante_defeso import FonteRendaDuranteDefeso
from .pescador_especialista import PescadorEspecialista

from decimal import Decimal

class RendaDuranteDefeso(models.Model):
    fonte = models.ForeignKey(
        FonteRendaDuranteDefeso,
        on_delete=models.PROTECT,
    )
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
        related_name='rendas_durante_defeso',
    )

    class Meta:
        unique_together = ['fonte', 'pescador_especialista']
        verbose_name = 'renda durante o defeso'
        verbose_name_plural = 'rendas durante o defeso'
