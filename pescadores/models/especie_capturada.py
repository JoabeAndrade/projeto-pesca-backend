from django.db import models
from .pescador import Pescador

ESPECIES_CAPTURADAS = [
    ('peixe', 'Peixes'),
    ('camarao', 'Camarão'),
    ('marisco', 'Marisco'),
    ('outras', 'Outras'),
]

class EspecieCapturadaDoPescador(models.Model):
    especie_capturada = models.CharField(choices=ESPECIES_CAPTURADAS, max_length=10, null=True)
    pescador = models.ForeignKey(Pescador, on_delete=models.CASCADE, related_name='especies_capturadas', null=True)

    def __str__(self):
        return self.especie_capturada
    
    def __repr__(self):
        return self.especie_capturada
