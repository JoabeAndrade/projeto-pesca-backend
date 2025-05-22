from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from pescadores.models import Colonia, Comunidade, Endereco, Municipio

class ColoniaTestes(TestCase):
    def setUp(self):
        self.municipio = self.create_municipio()
        self.comunidade = self.create_comunidade(municipio=self.municipio)
        self.endereco = self.create_endereco(municipio=self.municipio)

    def teste_dados_validos(self):
        colonia = Colonia(codigo='Z-01', comunidade=self.comunidade, endereco_sede=self.endereco)
        colonia.full_clean()

    def teste_codigo_obrigatorio(self):
        colonia = Colonia(comunidade=self.comunidade, endereco_sede=self.endereco)
        self.assertRaises(ValidationError, colonia.full_clean)

    def teste_codigo_tem_no_maximo_50_caracteres(self):
        params_list = [
            ('a' * 50, True),
            ('a' * 51, False),
        ]
        for params in params_list:
            colonia = Colonia(codigo=params[0], comunidade=self.comunidade, endereco_sede=self.endereco)
            with self.subTest(params):
                if params[1]:
                    colonia.full_clean()
                else:
                    self.assertRaises(ValidationError, colonia.full_clean)

    def teste_comunidade_obrigatoria(self):
        colonia = Colonia(codigo='Z-01', endereco_sede=self.endereco)
        self.assertRaises(ValidationError, colonia.full_clean)

    def teste_impossivel_excluir_comunidade_com_colonia_registrada(self):
        colonia = Colonia(comunidade=self.comunidade, endereco_sede=self.endereco)
        colonia.save()
        self.assertRaises(ProtectedError, self.comunidade.delete)

    def teste_endereco_sede_opcional(self):
        colonia = Colonia(codigo='Z-01', comunidade=self.comunidade)
        colonia.full_clean()

    def create_municipio(self, nome='Ilhéus', uf='BA'):
        return Municipio.objects.create(nome=nome, uf=uf)

    def create_comunidade(self, nome='Comunidade de Pescadores', municipio=None):
        if not municipio:
            municipio = self.create_municipio()
        return Comunidade.objects.create(nome=nome, municipio=municipio)

    def create_endereco(self,
        logradouro='Rua das Acácias',
        numero='123',
        bairro='Jardim Primavera',
        complemento='Bloco B, Apto 204',
        cep='30575320',
        municipio=None
    ):
        if not municipio:
            municipio = self.create_municipio()
        return Endereco.objects.create(
            logradouro=logradouro,
            numero=numero,
            bairro=bairro,
            complemento=complemento,
            cep=cep,
            municipio=municipio
        )
