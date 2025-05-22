from django.db import models
from django.core.validators import MinLengthValidator
from pescadores.validators import only_numeric_chars
from .municipio import Municipio

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, validators=[MinLengthValidator(8), only_numeric_chars], blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
