from django.db import models
from django.core.validators import MinValueValidator
from .pescador_especialista import PescadorEspecialista
from .relacao_parentesco import RelacaoParentesco

class ParentePescador(models.Model):
    relacao = models.ForeignKey(RelacaoParentesco, on_delete=models.PROTECT)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    especialista = models.ForeignKey(
        PescadorEspecialista,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ['especialista', 'relacao']
        verbose_name_plural = 'parentes pescadores'
