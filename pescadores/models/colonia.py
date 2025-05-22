from django.db import models
from .comunidade import Comunidade
from .endereco import Endereco

class Colonia(models.Model):
    codigo = models.CharField(max_length=50)
    comunidade = models.ForeignKey(Comunidade, related_name='comunidades', on_delete=models.PROTECT)
    endereco_sede = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)
