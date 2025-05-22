from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError
from pescadores.models import Endereco, Municipio

class TestesEndereco(TestCase):
    def teste_dados_validos(self):
        municipio = self.create_municipio_dados_validos()
        endereco = self.endereco_dados_validos(municipio=municipio)
        endereco.full_clean()

    def teste_logradouro_pode_ter_ate_100_caracteres(self):
        municipio = self.create_municipio_dados_validos()
        self.executar_teste_limite_maximo_de_caracteres('logradouro', 100, {'municipio': municipio})

    def teste_numero_pode_ter_ate_10_caracteres(self):
        municipio = self.create_municipio_dados_validos()
        self.executar_teste_limite_maximo_de_caracteres('numero', 10, {'municipio': municipio})

    def teste_bairro_pode_ter_ate_50_caracteres(self):
        municipio = self.create_municipio_dados_validos()
        self.executar_teste_limite_maximo_de_caracteres('bairro', 50, {'municipio': municipio})

    def teste_complemento_pode_ter_ate_100_caracteres(self):
        municipio = self.create_municipio_dados_validos()
        self.executar_teste_limite_maximo_de_caracteres('complemento', 100, {'municipio': municipio})

    def teste_complemento_opcional(self):
        municipio = self.create_municipio_dados_validos()
        endereco = self.endereco_dados_validos(complemento=None, municipio=municipio)
        endereco.full_clean()

    def teste_cep_deve_ter_exatamente_8_caracteres_numericos(self):
        municipio = self.create_municipio_dados_validos()
        params_list = [
            ('1020030', False),
            ('20300400', True),
            (30400500, True),
            ('4050060o', False),
            ('506007000', False),
        ]
        for params in params_list:
            with self.subTest(params):
                endereco = self.endereco_dados_validos(cep=params[0], municipio=municipio)
                if params[1]:
                    endereco.full_clean()
                else:
                    self.assertRaises(ValidationError, endereco.full_clean)

    def teste_cep_opcional(self):
        municipio = self.create_municipio_dados_validos()
        endereco = self.endereco_dados_validos(cep=None, municipio=municipio)
        endereco.full_clean()
    
    def teste_impossivel_excluir_municipio_com_endereco_registrado(self):
        municipio = self.create_municipio_dados_validos()
        endereco = self.endereco_dados_validos(municipio=municipio)
        endereco.save()
        self.assertRaises(ProtectedError, municipio.delete)

    def executar_teste_limite_maximo_de_caracteres(self, campo, limite, outros_params={}):
        params_list = [
            ('a' * limite, True),
            ('a' * (limite+1), False),
        ]
        for params in params_list:
            with self.subTest(params):
                params_sob_teste = {campo: params[0]}
                endereco = self.endereco_dados_validos(**params_sob_teste, **outros_params)
                if params[1]:
                    endereco.full_clean()
                else:
                    self.assertRaises(ValidationError, endereco.full_clean)

    def create_municipio_dados_validos(self, 
        nome_municipio='Belo Horizonte',
        uf_sigla='MG'
    ):
        return Municipio.objects.create(nome=nome_municipio, uf=uf_sigla)

    def endereco_dados_validos(self,
        logradouro='Rua das Acácias',
        numero='123',
        bairro='Jardim Primavera',
        complemento='Bloco B, Apto 204',
        cep='30575320',
        municipio=None
    ):
        return Endereco(
            logradouro=logradouro,
            numero=numero,
            bairro=bairro,
            complemento=complemento,
            cep=cep,
            municipio=municipio
        )
