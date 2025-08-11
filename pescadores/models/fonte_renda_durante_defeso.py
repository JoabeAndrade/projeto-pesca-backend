from django.db import models

class FonteRendaDuranteDefeso(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'fonte de renda durante o defeso'
        verbose_name_plural = 'fontes de renda durante o defeso'
