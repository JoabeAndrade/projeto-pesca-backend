from django.test import TestCase
from pescadores.models import AreaPesca
from django.core.exceptions import ValidationError

class TesteAreaPesca(TestCase):
    def teste_dados_validos(self):
        arte_pesca = AreaPesca(descricao='Emalhe')
        arte_pesca.full_clean()

    def teste_descricao_obrigatorio(self):
        area = AreaPesca()
        self.assertRaises(ValidationError, area.full_clean)

    def teste_descricao_tem_no_maximo_50_caracteres(self):
        area1 = AreaPesca(descricao='a' * 50)
        area1.full_clean()
        area2 = AreaPesca(descricao='a' * 51)
        self.assertRaises(ValidationError, area2.full_clean)
    
    def teste_descricao_deve_ser_unica(self):
        area1 = AreaPesca.objects.create(descricao='Mar')
        area2 = AreaPesca(descricao='Mar')
        self.assertRaises(ValidationError, area2.full_clean)
