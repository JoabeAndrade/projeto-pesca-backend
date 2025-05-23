from django.test import TestCase
from pescadores.models import Municipio
from pescadores.serializers import EnderecoSerializer

class TestesEnderecoSerializer(TestCase):
    def teste_dados_validos(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        s = EnderecoSerializer(data={
            'logradouro': 'Rua Arlindo Nogueira',
            'numero': '21',
            'bairro': 'Centro',
            'complemento': 'Apt. 101',
            'municipio': mun.id,
            'cep': '64000290',
        })
        self.assertTrue(s.is_valid())
    
    def teste_logradouro_obrigatorio(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        
        s = EnderecoSerializer(data={
            'numero': '21',
            'bairro': 'Centro',
            'complemento': 'Apt. 101',
            'municipio': mun.id,
            'cep': '64000290',
        })
        self.assertFalse(s.is_valid())
        self.assertTrue('logradouro' in s.errors.keys())

    def teste_numero_obrigatorio(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        s = EnderecoSerializer(data={
            'logradouro': 'Rua Arlindo Nogueira',
            'bairro': 'Centro',
            'complemento': 'Apt. 101',
            'municipio': mun.id,
            'cep': '64000290',
        })
        self.assertFalse(s.is_valid())

    def teste_bairro_obrigatorio(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        s = EnderecoSerializer(data={
            'logradouro': 'Rua Arlindo Nogueira',
            'numero': '21',
            'complemento': 'Apt. 101',
            'municipio': mun.id,
            'cep': '64000290',
        })
        self.assertFalse(s.is_valid())

    def teste_complemento_opcional(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        s = EnderecoSerializer(data={
            'logradouro': 'Rua Arlindo Nogueira',
            'numero': '21',
            'bairro': 'Centro',
            'municipio': mun.id,
            'cep': '64000290',
        })
        self.assertTrue(s.is_valid())

    def teste_municipio_obrigatorio(self):
        s = EnderecoSerializer(data={
            'logradouro': 'Rua Arlindo Nogueira',
            'numero': '21',
            'bairro': 'Centro',
            'complemento': 'Apt. 101',
            'cep': '64000290',
        })
        self.assertFalse(s.is_valid())
        self.assertTrue('municipio' in s.errors.keys())

    def teste_cep_opcional(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        s = EnderecoSerializer(data={
            'logradouro': 'Rua Arlindo Nogueira',
            'numero': '21',
            'bairro': 'Centro',
            'complemento': 'Apt. 101',
            'municipio': mun.id,
        })
        self.assertTrue(s.is_valid())
