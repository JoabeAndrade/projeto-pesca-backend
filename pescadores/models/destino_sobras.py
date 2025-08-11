from django.db import models

class DestinoSobras(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'destino das sobras'
        verbose_name_plural = 'destinos das sobras'
