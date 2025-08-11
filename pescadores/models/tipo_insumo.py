from django.db import models

class TipoInsumo(models.Model):
    descricao = models.CharField('descrição', max_length=50, unique=True)

    def __str__(self):
        return self.descricao

    def __repr__(self):
        return self.descricao

    class Meta:
        verbose_name = 'tipo de insumo'
        verbose_name_plural = 'tipos de insumo'
        ordering = ['descricao']
