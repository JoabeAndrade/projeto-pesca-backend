from django.db import models

class HabilidadeOutraArea(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'habilidade em outra área'
        verbose_name_plural = 'habilidades em outras áreas'
