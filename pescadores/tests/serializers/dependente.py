from django.test import TestCase
from pescadores.serializers import DependenteSerializer

class TesteCriarDependente(TestCase):
    fixtures = ['pescadores']

    def teste_dados_validos(self):
        dados = {'relacao': 'conjuge_companheira', 'quantidade': 1, 'pescador': 1}
        serializer = DependenteSerializer(data=dados)
        self.assertTrue(serializer.is_valid())
    
    def teste_relacao_obrigatorio(self):
        dados = {'quantidade': 2, 'pescador': 2}
        serializer = DependenteSerializer(data=dados)
        self.assertFalse(serializer.is_valid())

    def teste_relacao_invalido(self):
        dados = {'relacao': 'inexistente', 'quantidade': 1, 'pescador': 1}
        serializer = DependenteSerializer(data=dados)
        self.assertFalse(serializer.is_valid())

    def teste_quantidade_obrigatoria(self):
        dados = {'relacao': 'sogra', 'pescador': 1}
        serializer = DependenteSerializer(data=dados)
        self.assertFalse(serializer.is_valid())

    def teste_quantidade_deve_ser_positiva(self):
        dados = {'relacao': 'pais_avos_bisavos', 'quantidade': -4, 'pescador': 2}
        serializer = DependenteSerializer(data=dados)
        self.assertFalse(serializer.is_valid())

    def teste_quantidade_deve_ser_maior_que_zero(self):
        dados = {'relacao': 'pais_avos_bisavos', 'quantidade': 0, 'pescador': 2}
        serializer = DependenteSerializer(data=dados)
        self.assertFalse(serializer.is_valid())
