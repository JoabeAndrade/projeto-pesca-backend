from django.db import models

class AlternativaRenda(models.Model):
    descricao = models.CharField('descrição', max_length=100, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'alternativa de renda'
        verbose_name_plural = 'alternativas de renda'
        ordering = ['descricao']
