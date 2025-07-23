from django.db import models

class ProgramaSocial(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome
