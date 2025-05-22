from django.db import models

class AreaPesca(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'areas pesca'
