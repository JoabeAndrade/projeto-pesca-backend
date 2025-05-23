import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from pescadores.models import Pescador
from pescadores.serializers import PescadorSerializer

class TesteListarTodosPescadores(TestCase):
    fixtures = ['pescadores']

    def teste_listar_pescadores(self):
        response = self.client.get(reverse('pescador_list'))
        pescadores = Pescador.objects.all()
        serializer = PescadorSerializer(pescadores, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TesteVerPescador(TestCase):
    fixtures = ['pescadores']

    def teste_get_pescador(self):
        response = self.client.get(reverse('pescador_detail', kwargs={'pk': 1}))
        pescador = Pescador.objects.get(pk=1)
        serializer = PescadorSerializer(pescador)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def teste_visualizar_pescador_inexistente(self):
        response = self.client.get(reverse('pescador_detail', kwargs={'pk': 9}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TesteInserirPescador(TestCase):
    def setUp(self):
        self.valid_payload = {
            'nome': 'Adalberto de Tal',
            'sexo': 'm',
            'apelido': 'Dadinho',
            'data_nascimento': '1980-12-30',
            'nome_pai': 'Fulano de Tal',
            'nome_mae': 'Fulana de Tal',
            'data_inscricao_colonia': '2015-06-02',
            'rg': 'mg123456789',
            'cpf': 11122233344,
            'tipo_embarcacao': 'barco',
            'tamanho_embarcacao': 'grande',
            'proprietario_embarcacao': False,
            'escolaridade': 'medio_completo',
            'renda_mensal_pesca': 950.25,
            'outra_renda': 'Aluguel',
            'ativo': True,
            'motivo_inatividade': None,
            'falecido': False,
            'data_cadastramento': '2024-01-11',
        }
        self.invalid_payload = {'nome': 'Abílio', 'sexo': 'z'}
    
    def test_create_valid_pescador(self):
        response = self.client.post(reverse('pescador_list'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_pescador(self):
        response = self.client.post(reverse('pescador_list'), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TesteEditarPescador(TestCase):
    fixtures = ['pescadores']

    def setUp(self):
        self.valid_payload = {'nome': 'João', 'sexo': 'm'}
        self.invalid_payload = {'nome': 'João', 'sexo': 'z'}
    
    def teste_edita_pescador_dados_validos(self):
        response = self.client.put(
            path=reverse('pescador_detail', kwargs={'pk': 2}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def teste_edita_pescador_dados_invalidos(self):
        response = self.client.put(
            path=reverse('pescador_detail', kwargs={'pk': 2}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TesteExcluirPescador(TestCase):
    fixtures = ['pescadores']

    def teste_excluir_pescador(self):
        response = self.client.delete(reverse('pescador_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
