from django.test import TestCase
from django.core.exceptions import ValidationError
from pescadores.models import Dependente
from unittest import skip
from pescadores.tests.utils import create_pescador_dados_validos

class DependenteTestes(TestCase):
    def setUp(self):
        self.pescador = create_pescador_dados_validos()

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
