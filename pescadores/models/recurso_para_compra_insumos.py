from django.db import models

class RecursoParaCompraInsumos(models.Model):
    descricao = models.CharField('descrição', max_length=50, unique=True)

    def __str__(self):
        return self.descricao

    def __repr__(self):
        return self.descricao

    class Meta:
        verbose_name = 'recurso para compra de insumos'
        verbose_name_plural = 'recursos para compra de insumos'
        ordering = ['descricao']
