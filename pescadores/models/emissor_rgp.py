from django.db import models

class EmissorRgp(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'emissor do RGP'
        verbose_name_plural = 'emissores de RGP'
