from django.db import models

class ArtePesca(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'artes pesca'
