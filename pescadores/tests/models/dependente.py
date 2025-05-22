from django.test import TestCase
from django.core.exceptions import ValidationError
from pescadores.models import Dependente, Pescador
from datetime import date
from decimal import Decimal
from unittest import skip

class DependenteTestes(TestCase):
    def setUp(self):
        self.pescador = self.create_pescador_dados_validos()

    def teste_dados_validos(self):
        dependente = Dependente(relacao='filhos_enteados', quantidade=2, pescador=self.pescador)
        dependente.full_clean()
        dependente.save()

    def teste_relacao_obrigatoria(self):
        dependente = Dependente(quantidade=2, pescador=self.pescador)
        self.assertRaises(ValidationError, dependente.full_clean)

    def teste_quantidade_obrigatoria(self):
        dependente = Dependente(relacao='filhos_enteados', pescador=self.pescador)
        self.assertRaises(ValidationError, dependente.full_clean)

    def teste_quantidade_deve_ser_positiva(self):
        dependente = Dependente(relacao='filhos_enteados', quantidade=-1, pescador=self.pescador)
        self.assertRaises(ValidationError, dependente.full_clean)

    def teste_quantidade_deve_ser_maior_que_zero(self):
        dependente = Dependente(relacao='filhos_enteados', quantidade=0, pescador=self.pescador)
        self.assertRaises(ValidationError, dependente.full_clean)

    def teste_pescador_obrigatorio(self):
        dependente = Dependente(relacao='filhos_enteados', quantidade=2)
        self.assertRaises(ValidationError, dependente.full_clean)
    
    @skip
    def teste_excluir_pescador_exclui_os_dependentes(self):
        dependente = Dependente.objects.create(relacao='filhos_enteados', quantidade=2, pescador=self.pescador)
        self.pescador.delete()
        self.assertIsNone(dependente.id)

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
