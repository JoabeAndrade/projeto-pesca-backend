from django.db import models

class MotivacaoPesca(models.Model):
    descricao = models.CharField(max_length=100)

    def __repr__(self):
        return self.descricao
    
    def __str__(self):
        return self.descricao
