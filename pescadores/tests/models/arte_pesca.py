from django.test import TestCase
from pescadores.models import ArtePesca
from django.core.exceptions import ValidationError

class TesteArtePesca(TestCase):
    def teste_dados_validos(self):
        arte_pesca = ArtePesca(nome='Emalhe')
        arte_pesca.full_clean()

    def teste_nome_obrigatorio(self):
        ap = ArtePesca()
        self.assertRaises(ValidationError, ap.full_clean)

    def teste_nome_tem_no_maximo_50_caracteres(self):
        ap1 = ArtePesca(nome='a' * 50)
        ap1.full_clean()
        ap2 = ArtePesca(nome='a' * 51)
        self.assertRaises(ValidationError, ap2.full_clean)
    
    def teste_nome_deve_ser_unico(self):
        ap1 = ArtePesca.objects.create(nome='Arrasto de Fundo')
        ap2 = ArtePesca(nome='Arrasto de Fundo')
        self.assertRaises(ValidationError, ap2.full_clean)
