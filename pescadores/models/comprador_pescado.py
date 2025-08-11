from django.db import models

class CompradorPescado(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'comprador do pescado'
        verbose_name_plural = 'compradores do pescado'
