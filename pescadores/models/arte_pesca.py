from django.db import models

class ArtePesca(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'artes pesca'
