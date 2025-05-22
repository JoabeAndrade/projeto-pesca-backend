from django.test import TestCase
from pescadores.models import Pescador, Telefone
from datetime import date
from decimal import Decimal
from django.core.exceptions import ValidationError
from unittest import skip

class TestesPescador(TestCase):
    def setUp(self):
        self.pescador = self.create_pescador_dados_validos()

    def teste_dados_validos(self):
        telefone = Telefone(numero='123456789', pescador=self.pescador)
        telefone.full_clean()
        telefone.save()

    def teste_numero_obrigatorio(self):
        telefone = Telefone(pescador=self.pescador)
        self.assertRaises(ValidationError, telefone.full_clean)

    def teste_numero_tem_no_maximo_20_caracteres(self):
        param_list = [
            ('', False),
            (None, False),
            ('1' * 20, True),
            ('1' * 21, False),
        ]
        for params in param_list:
            with self.subTest(params):
                telefone = Telefone(numero=params[0], pescador=self.pescador)
                if params[1]:
                    telefone.full_clean()
                else:
                    self.assertRaises(ValidationError, telefone.full_clean)

    def teste_numero_caracteres_sao_todos_numericos(self):
        param_list = [
            ('123456789', True),
            ('12345-6789', False),
            ('abcdefghi', False),
            ('123a56789', False),
            (123456789, True),
        ]
        for params in param_list:
            with self.subTest(params):
                telefone = Telefone(numero=params[0], pescador=self.pescador)
                if params[1]:
                    telefone.full_clean()
                else:
                    self.assertRaises(ValidationError, telefone.full_clean)

    def teste_pescador_obrigatorio(self):
        telefone = Telefone(numero='123456789')
        self.assertRaises(ValidationError, telefone.full_clean)

    @skip
    def teste_apagar_pescador_apaga_os_telefones(self):
        t1 = Telefone.objects.create(numero='123456789', pescador=self.pescador)
        t2 = Telefone.objects.create(numero='321654987', pescador=self.pescador)
        assert t1.id == 1
        assert t2.id == 2
        self.pescador.delete()
        self.assertIsNone(t1.id)
        self.assertIsNone(t2.id)

    def create_pescador_dados_validos(self,
        nome="João da Silva",
        sexo="m",
        apelido="Joãozinho",
        data_nascimento=date(1980, 5, 12),
        nome_pai="Pedro da Silva",
        nome_mae="Maria das Dores",
        rg="123456789",
        cpf="12345678901",
        matricula_colonia="12345",
        data_inscricao_colonia=date(2005, 7, 1),
        tipo_embarcacao="canoa",
        tamanho_embarcacao="pequeno",
        proprietario_embarcacao=True,
        escolaridade="fundamental_completo",
        renda_mensal_pesca=Decimal("1500.00"),
        outra_renda="Trabalho rural",
        ativo=True,
        motivo_inatividade="",
        falecido=False,
        data_cadastramento=date.today(),
    ):
        return Pescador.objects.create(
            nome=nome,
            sexo=sexo,
            apelido=apelido,
            data_nascimento=data_nascimento,
            nome_pai=nome_pai,
            nome_mae=nome_mae,
            rg=rg,
            cpf=cpf,
            matricula_colonia=matricula_colonia,
            data_inscricao_colonia=data_inscricao_colonia,
            tipo_embarcacao=tipo_embarcacao,
            tamanho_embarcacao=tamanho_embarcacao,
            proprietario_embarcacao=proprietario_embarcacao,
            escolaridade=escolaridade,
            renda_mensal_pesca=renda_mensal_pesca,
            outra_renda=outra_renda,
            ativo=ativo,
            motivo_inatividade=motivo_inatividade,
            falecido=falecido,
            data_cadastramento=data_cadastramento,
        )
