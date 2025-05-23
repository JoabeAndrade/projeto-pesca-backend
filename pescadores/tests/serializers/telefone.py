from django.test import TestCase
from pescadores.serializers import TelefoneSerializer

class TelefoneSerializerTest(TestCase):
    fixtures = ['pescadores']

    def teste_inserir_dados_validos(self):
        s = TelefoneSerializer(data={
            'numero': '1212341234',
            'pescador': 2,
        })
        self.assertTrue(s.is_valid())

    def teste_telefone_deve_possuir_apenas_caracteres_numericos(self):
        params_list = [
            ('11222223333', True),
            (11222223333, True),
            ('(11) 22222-3333', False),
            ('11a22223333', False),
        ]
        for params in params_list:
            with self.subTest(params):
                s = TelefoneSerializer(data={'numero': params[0], 'pescador': 1})
                self.assertEqual(s.is_valid(), params[1])
