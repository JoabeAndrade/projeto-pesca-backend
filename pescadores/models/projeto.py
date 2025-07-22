from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.nome
