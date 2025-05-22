from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError
from pescadores.models import Pescador, Municipio, Comunidade, Colonia
from datetime import date
from decimal import Decimal

class PescadorTestes(TestCase):
    def teste_dados_validos(self):
        pescador = self.novo_pescador_dados_validos()
        pescador.full_clean()

    def teste_nome_obrigatorio(self):
        p1 = self.novo_pescador_dados_validos(nome=None)
        p2 = self.novo_pescador_dados_validos(nome='')
        self.assertRaises(ValidationError, p1.full_clean)
        self.assertRaises(ValidationError, p2.full_clean)

    def teste_nome_deve_ter_entre_2_e_100_caracteres(self):
        param_list = [
            ('a' * 1, False),
            ('a' * 2, True),
            ('a' * 100, True),
            ('a' * 101, False),
        ]
        for params in param_list:
            with self.subTest(params):
                pescador = self.novo_pescador_dados_validos(nome=params[0])
                if params[1]:
                    pescador.full_clean()
                else:
                    self.assertRaises(ValidationError, pescador.full_clean)

    def teste_todos_outros_atributos_sao_opcionais(self):
        pescador = Pescador(nome='João da Silva')
        pescador.full_clean()

    def teste_nome_apelido_ter_entre_2_e_100_caracteres(self):
        param_list = [
            ('a' * 1, False),
            ('a' * 2, True),
            ('a' * 100, True),
            ('a' * 101, False),
        ]
        for params in param_list:
            with self.subTest(params):
                pescador = self.novo_pescador_dados_validos(apelido=params[0])
                if params[1]:
                    pescador.full_clean()
                else:
                    self.assertRaises(ValidationError, pescador.full_clean)

    def teste_nome_do_pai_deve_ter_entre_2_e_100_caracteres(self):
        param_list = [
            ('a' * 1, False),
            ('a' * 2, True),
            ('a' * 100, True),
            ('a' * 101, False),
        ]
        for params in param_list:
            with self.subTest(params):
                pescador = self.novo_pescador_dados_validos(nome_pai=params[0])
                if params[1]:
                    pescador.full_clean()
                else:
                    self.assertRaises(ValidationError, pescador.full_clean)

    def teste_nome_da_mae_deve_ter_entre_2_e_100_caracteres(self):
        param_list = [
            ('a' * 1, False),
            ('a' * 2, True),
            ('a' * 100, True),
            ('a' * 101, False),
        ]
        for params in param_list:
            with self.subTest(params):
                pescador = self.novo_pescador_dados_validos(nome_mae=params[0])
                if params[1]:
                    pescador.full_clean()
                else:
                    self.assertRaises(ValidationError, pescador.full_clean)

    def teste_municipio_nao_pode_ser_excluido_se_houver_pescador_natural(self):
        municipio = Municipio.objects.create(nome='Nome do Município', uf='SP')
        pescador = self.novo_pescador_dados_validos()
        pescador.naturalidade = municipio
        pescador.save()
        self.assertRaises(ProtectedError, municipio.delete)

    def teste_rg_deve_ter_menos_de_20_caracteres(self):
        p1 = self.novo_pescador_dados_validos(rg='a' * 20)
        p2 = self.novo_pescador_dados_validos(rg='a' * 21)
        p1.full_clean()
        self.assertRaises(ValidationError, p2.full_clean)

    def teste_cpf_deve_ter_11_caracteres_numericos(self):
        param_list = [
            ('1', False),
            ('11122233344', True),
            ('11122a33344', False),
            ('11122 33344', False),
            ('111222333445', False),
        ]
        for params in param_list:
            with self.subTest(params):
                pescador = self.novo_pescador_dados_validos(cpf=params[0])
                if params[1]:
                    pescador.full_clean()
                else:
                    self.assertRaises(ValidationError, pescador.full_clean)

    def teste_matricula_colonia_pode_ter_no_maximo_20_caracteres(self):
        p1 = self.novo_pescador_dados_validos(matricula_colonia='1' * 20)
        p2 = self.novo_pescador_dados_validos(matricula_colonia='1' * 21)
        p1.full_clean()
        self.assertRaises(ValidationError, p2.full_clean)

    def teste_matricula_colonia_pode_apenas_ter_caracteres_numericos(self):
        param_list = [
            ('11112222333344445555', True),
            ('111i2222333344445555', False),
            ('111122 1333344445555', False),
            (11112222333344445555, True),
        ]
        for params in param_list:
            with self.subTest(params):
                pescador = self.novo_pescador_dados_validos(matricula_colonia=params[0])
                if params[1]:
                    pescador.full_clean()
                else:
                    self.assertRaises(ValidationError, pescador.full_clean)

    def teste_renda_mensal_pesca_nao_pode_ser_negativo(self):
        p1 = self.novo_pescador_dados_validos(renda_mensal_pesca=1000)
        p2 = self.novo_pescador_dados_validos(renda_mensal_pesca=0)
        p3 = self.novo_pescador_dados_validos(renda_mensal_pesca=-1000)
        p1.full_clean()
        p2.full_clean()
        self.assertRaises(ValidationError, p3.full_clean)

    def teste_outra_renda_tem_no_maximo_50_caracteres(self):
        p1 = self.novo_pescador_dados_validos(outra_renda='a' * 50)
        p2 = self.novo_pescador_dados_validos(outra_renda='a' * 51)
        p1.full_clean()
        self.assertRaises(ValidationError, p2.full_clean)

    def teste_falecido_falso_por_default(self):
        p1 = self.novo_pescador_dados_validos(falecido=True)
        p2 = self.novo_pescador_dados_validos(falecido=None)
        p1.save()
        p2.save()
        self.assertTrue(p1.falecido)
        self.assertFalse(p2.falecido)

    def teste_colonia_nao_pode_ser_excluida_se_houver_pescador_registrado(self):
        mun = Municipio.objects.create(nome='Ilhéus', uf='BA')
        com = Comunidade.objects.create(nome='Beira-Mar', municipio=mun)
        colonia = Colonia.objects.create(codigo='Z-01', comunidade=com)
        pescador = self.novo_pescador_dados_validos()
        pescador.colonia = colonia
        pescador.save()
        self.assertRaises(ProtectedError, colonia.delete)

    def novo_pescador_dados_validos(self,
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
        return Pescador(
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
