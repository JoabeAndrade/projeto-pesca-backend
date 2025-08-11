from django.db import models

class RelacaoParentesco(models.Model):
    descricao = models.CharField(max_length=50)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'relação de parentesco'
        verbose_name_plural = 'relações de parentesco'
