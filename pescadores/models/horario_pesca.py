from django.db import models

class HorarioPesca(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'horário de pesca'
        verbose_name_plural = 'horários de pesca'
