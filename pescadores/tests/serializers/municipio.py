from django.test import TestCase
from pescadores.serializers import MunicipioSerializer

class TesteMunicipioSerializer(TestCase):
    def teste_dados_validos(self):
        s = MunicipioSerializer(data={'nome': 'Itabuna', 'uf': 'BA'})
        self.assertTrue(s.is_valid())
    
    def teste_nome_obrigatorio(self):
        s = MunicipioSerializer(data={'uf': 'BA'})
        self.assertFalse(s.is_valid())

    def teste_uf_obrigatoria(self):
        s = MunicipioSerializer(data={'nome': 'Itabuna'})
        self.assertFalse(s.is_valid())

    def teste_nomes_invalidos(self):
        params_list = [
            ('Nome Válido', True),
            ('', False),
            (None, False),
            (' ', False),
        ]
        for params in params_list:
            with self.subTest(params):
                s = MunicipioSerializer(data={'nome': params[0], 'uf': 'BA'})
                self.assertEqual(s.is_valid(), params[1])

    def teste_ufs_invalidas(self):
        params_list = [
            ('BA', True),
            ('ba', False),
            ('B', False),
            ('BAA', False),
            ('', False),
            (None, False),
            ('ZT', False),
        ]
        for params in params_list:
            with self.subTest(params):
                s = MunicipioSerializer(data={'nome': 'Springfield', 'uf': params[0]})
                self.assertEqual(s.is_valid(), params[1])

    def teste_combinacao_nome_uf_unica(self):
        s1 = MunicipioSerializer(data={'nome': 'Springfield', 'uf': 'PE'})
        s2 = MunicipioSerializer(data={'nome': 'Springfield', 'uf': 'PE'})
        s3 = MunicipioSerializer(data={'nome': 'Springfield', 'uf': 'BA'})
        s1.is_valid()
        s1.save()
        self.assertFalse(s2.is_valid())
        self.assertTrue(s3.is_valid())
