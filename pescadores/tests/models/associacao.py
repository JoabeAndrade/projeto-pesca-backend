from django.test import TestCase
from django.core.exceptions import ValidationError
from pescadores.models import Associacao, Endereco, Municipio
from unittest import skip

class AssociacaoTeste(TestCase):
    def teste_dados_validos(self):
        endereco = self.create_endereco_valido()
        associacao = Associacao(nome="Nome da Associacao", endereco=endereco)
        associacao.full_clean()

    def teste_nome_obrigatorio(self):
        endereco = self.create_endereco_valido()
        associacao = Associacao(endereco=endereco)
        self.assertRaises(ValidationError, associacao.full_clean)

    def teste_nome_tem_no_maximo_100_caracteres(self):
        endereco = self.create_endereco_valido()
        params_list = [
            ('a' * 100, True),
            ('a' * 101, False),
        ]
        for params in params_list:
            with self.subTest(params):
                associacao = Associacao(nome=params[0], endereco=endereco)
                if params[1]:
                    associacao.full_clean()
                else:
                    self.assertRaises(ValidationError, associacao.full_clean)

    def teste_endereco_opcional(self):
        associacao = Associacao(nome='Associação de Pescadores')
        associacao.full_clean()

    @skip
    def teste_excluir_associacao_exclui_endereco(self):
        endereco = self.create_endereco_valido()
        associacao = Associacao.objects.create(nome='Associação de Pescadores', endereco=endereco)
        associacao.delete()
        self.assertIsNone(endereco.id)

    def create_endereco_valido(self):
        municipio = Municipio.objects.create(
            nome='Ilhéus',
            uf='BA'
        )
        return Endereco.objects.create(
            logradouro='Rua das Acácias',
            numero='123',
            bairro='Jardim Primavera',
            complemento='Bloco B, Apto 204',
            cep='30575320',
            municipio=municipio
        )
