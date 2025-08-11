from django.db import models

class FornecedorInsumos(models.Model):
    descricao = models.CharField(max_length=100)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'fornecedor de insumos'
        verbose_name_plural = 'fornecedores de insumos'
