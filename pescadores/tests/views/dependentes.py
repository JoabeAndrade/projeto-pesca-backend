from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class TesteInserirDependente(TestCase):
    fixtures = ['pescadores']

    def teste_inserir_com_dados_validos(self):
        response = self.client.post(
            path=reverse('dependente_list'),
            data=JSONRenderer().render({
                'relacao': 'conjuge_companheira',
                'quantidade': 1,
                'pescador': 1,
            }),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def teste_pescador_nao_existe(self):
        response = self.client.delete(
            path=reverse('dependente_detail', kwargs={'pk': 99}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
