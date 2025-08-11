from django.db import models

class BeneficioColonia(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'benefício da colônia'
        verbose_name_plural = 'benefícios da colônia'
