from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError
from pescadores.models import Comunidade, Municipio

class ComunidadeTestes(TestCase):
    def teste_dados_validos(self):
        municipio = Municipio.objects.create(nome='Ilheus', uf='BA')
        comunidade = Comunidade(nome='Nome da Comunidade', municipio=municipio)
        comunidade.full_clean()

    def teste_nome_obrigatorio(self):
        municipio = Municipio.objects.create(nome='Ilheus', uf='BA')
        comunidade = Comunidade(nome='', municipio=municipio)
        self.assertRaises(ValidationError, comunidade.full_clean)

    def teste_nome_tem_no_maximo_100_caracteres(self):
        municipio = Municipio.objects.create(nome='Ilheus', uf='BA')
        params_list = [
            ('a' * 100, True),
            ('a' * 101, False),
        ]
        for params in params_list:
            with self.subTest(params):
                associacao = Comunidade(nome=params[0], municipio=municipio)
                if params[1]:
                    associacao.full_clean()
                else:
                    self.assertRaises(ValidationError, associacao.full_clean)

    def teste_municipio_obrigatorio(self):
        comunidade = Comunidade(nome='Nome da Comunidade', municipio=None)
        self.assertRaises(ValidationError, comunidade.full_clean)

    def teste_nao_pode_deletar_municipio_com_comunidade_registrada(self):
        municipio = Municipio.objects.create(nome='Ilheus', uf='BA')
        Comunidade.objects.create(nome='Nome da Comunidade', municipio=municipio)
        self.assertRaises(ProtectedError, municipio.delete)
