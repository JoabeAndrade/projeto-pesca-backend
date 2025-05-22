from django.db import models
from pescadores.models import Pescador
from django.core.validators import MinValueValidator

TIPOS_DEPENDENTE = [
    ('conjuge_companheira', 'Cônjuge ou companheiro(a)'),
    ('filhos_enteados', 'Filhos(as) ou enteados(as)'),
    ('irmaos_netos_bisnetos', 'Irmãos(ãs), netos(as) ou bisnetos(as)'),
    ('pais_avos_bisavos', 'Pais, avós ou bisavós'),
    ('sogro', 'Sogro(a)'),
    ('incapazes', 'Incapaz(es)'),
]

class Dependente(models.Model):
    relacao = models.CharField(max_length=30, choices=TIPOS_DEPENDENTE)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    pescador = models.ForeignKey(Pescador, on_delete=models.CASCADE, related_name='dependentes')
