from django.db import models
from django.db.models.constraints import UniqueConstraint
from .pescador import Pescador

VALORES = (
    ('nd', 'Não declarado'),
    ('subsitencia', 'Subsistência'),
    ('meio', 'Até 1/2 salário mínimo'),
    ('meio_um', 'De 1/2 a 1 salário mínimo'),
    ('um', '1 salário mínimo'),
    ('dois', 'De 1 a 2 salários mínimos'),
    ('tres', 'De 2 a 3 salários mínimos'),
    ('quatro', 'De 3 a 4 salários mínimos'),
    ('cinco', 'De 4 a 5 salários mínimos'),
    ('mais', 'Maior que 5 salários mínimos'),
)

FONTES = (
    ('pesca', 'Pesca'),
    ('agricultura', 'Agricultor(a)'),
    ('aposentadoria', 'Aposentado(a)'),
    ('comerciante', 'Comerciante'),
    ('construcao_civil', 'Contrução civil'),
    ('faxina', 'Diarista/faxineiro(a)'),
    ('mecanica', 'Mecânico(a)'),
)

class Renda(models.Model):
    pescador = models.ForeignKey(Pescador, on_delete=models.CASCADE, related_name='rendas', null=True, blank=False)
    valor = models.CharField(choices=VALORES, max_length=20, null=True, blank=False)
    fonte = models.CharField(choices=FONTES, max_length=20, null=True, blank=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['pescador', 'fonte'], name='unique_pescador_fonte_constraint')
        ]
