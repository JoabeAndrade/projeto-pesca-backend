from django.db import models

class AtividadeAnterior(models.Model):
    descricao = models.CharField(max_length=50)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao
