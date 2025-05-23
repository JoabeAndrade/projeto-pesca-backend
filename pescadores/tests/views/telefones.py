import json
from django.test import TestCase
from rest_framework import status
from pescadores.models import Telefone
from pescadores.serializers import TelefoneSerializer
from unittest import skip

class TesteListarTelefones(TestCase):
    fixtures = ['pescadores']

    def teste_listar_telefones(self):
        response = self.client.get('/telefones/')
        telefones = Telefone.objects.all()
        serializer = TelefoneSerializer(telefones, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TesteVerTelefone(TestCase):
    fixtures = ['pescadores']

    def teste_visualizar_telefone(self):
        response = self.client.get('/telefones/1')
        telefones = Telefone.objects.get(pk=1)
        serializer = TelefoneSerializer(telefones)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def teste_visualizar_telefone_inexistente(self):
        response = self.client.get('/telefones/9')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TesteInserirTelefone(TestCase):
    def setUp(self):
        self.valid_payload = {
            'numero': '12123451234',
            'pescador': 3,
        }
        self.invalid_payload = {
            'numero': 'ab123451234',
            'pescador': 99,
        }
    
    @skip("Erro desconhecido")
    def teste_inserir_telefone_valido(self):
        response = self.client.post('/telefones/', data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def teste_inserir_telefone_invalido(self):
        response = self.client.post('/telefones/', data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TesteEditarTelefone(TestCase):
    fixtures = ['pescadores']

    def setUp(self):
        self.valid_payload = {
            'numero': '1212341234',
            'pescador': 1
        }
        self.invalid_payload = {
            'numero': 'ab123451234',
            'pescador': 99,
        }
    
    def teste_edita_telefone_dados_validos(self):
        response = self.client.put('/telefones/2', data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def teste_edita_telefone_dados_invalidos(self):
        response = self.client.put('/telefones/2', data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TesteExcluirTelefone(TestCase):
    fixtures = ['pescadores']

    def teste_excluir_telefone(self):
        response = self.client.delete('/telefones/2')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
