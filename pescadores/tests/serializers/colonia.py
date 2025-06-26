from django.test import TestCase
from pescadores.models import Comunidade, Municipio, Endereco
from pescadores.serializers import ColoniaSerializer
from unittest import skip

class TestesColoniaSerializer(TestCase):
    def setUp(self):
        self.mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        self.com = Comunidade.objects.create(nome='Uma Comunidade', municipio=self.mun)
        self.end = Endereco.objects.create(
            logradouro='Rua Arlindo Nogueira',
            numero='21',
            bairro='Centro',
            complemento='Apt. 101',
            municipio=self.mun,
            cep='64000290',
        )
        return super().setUp()

    def teste_dados_validos(self):
        s = ColoniaSerializer(data={
            'codigo': 'COL-64',
            'comunidade_id': self.com.id,
            'endereco_sede_id': self.end.id,
        })
        self.assertTrue(s.is_valid())

    def teste_codigo_obrigatorio(self):
        s = ColoniaSerializer(data={
            'comunidade_id': self.com.id,
            'endereco_sede_id': self.end.id,
        })
        self.assertFalse(s.is_valid())
        self.assertTrue('codigo' in s.errors.keys())

    def teste_comunidade_id_obrigatorio(self):
        s = ColoniaSerializer(data={
            'codigo': 'COL-64',
            'endereco_sede_id': self.end.id,
        })
        self.assertFalse(s.is_valid())
        self.assertTrue('comunidade_id' in s.errors.keys())

    def teste_endereco_sede_id_opcional(self):
        s = ColoniaSerializer(data={
            'codigo': 'COL-64',
            'comunidade_id': self.com.id,
        })
        self.assertTrue(s.is_valid())
