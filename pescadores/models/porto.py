from django.db import models

class Porto(models.Model):
    nome = models.CharField(max_length=100)

    def __repr__(self):
        return self.nome
