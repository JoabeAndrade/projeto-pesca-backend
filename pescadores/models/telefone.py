from django.db import models
from pescadores.validators import only_numeric_chars
from .pescador import Pescador

class Telefone(models.Model):
    numero = models.CharField(max_length=20, validators=[only_numeric_chars])
    pescador = models.ForeignKey(Pescador, related_name='telefones', on_delete=models.CASCADE)
