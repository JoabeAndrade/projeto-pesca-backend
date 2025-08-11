from django.db import models

class ItemEstruturaResidencial(models.Model):
    descricao = models.CharField(max_length=50)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'item de estrutura residencial'
        verbose_name_plural = 'itens de estrutura residencial'
