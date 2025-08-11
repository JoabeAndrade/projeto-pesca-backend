from django.test import TestCase
from pescadores.serializers import PescadorSerializer
from pescadores.tests.utils import get_or_create_porto_dados_validos

class TestePescadorSerializer(TestCase):
    def setUp(self):
        self.porto = get_or_create_porto_dados_validos()

    def teste_nome_obrigatorio(self):
        data_com_nome = {'nome': 'Fulano de Tal', 'porto_desembarque_principal': self.porto.id}
        data_sem_nome = {'porto_desembarque_principal': self.porto.id}
        data_nome_blank = {'nome': '', 'porto_desembarque_principal': self.porto.id}
        s1 = PescadorSerializer(data=data_com_nome)
        s2 = PescadorSerializer(data=data_sem_nome)
        s3 = PescadorSerializer(data=data_nome_blank)
        self.assertTrue(s1.is_valid())
        self.assertFalse(s2.is_valid())
        self.assertFalse(s3.is_valid())

    def teste_nome_deve_ter_entre_2_e_100_caracteres(self):
        param_list = [
            ('a'*1, False),
            ('a'*2, True),
            ('a'*100, True),
            ('a'*101, False),
        ]
        for params in param_list:
            with self.subTest(params):
                s = PescadorSerializer(data={'nome': params[0], 'porto_desembarque_principal': self.porto.id})
                self.assertEqual(s.is_valid(), params[1])

    def teste_sexo_aceita_apenas_m_ou_f(self):
        param_list = [
            ('m', True),
            ('f', True),
            ('z', False),
            ('a', False),
            (1, False),
            ('mm', False),
            ('mf', False),
        ]
        for params in param_list:
            with self.subTest(params):
                s = PescadorSerializer(data={
                    'nome': 'Fulano',
                    'sexo': params[0],
                    'porto_desembarque_principal': self.porto.id,
                })
                self.assertEqual(s.is_valid(), params[1])

    def teste_apelido_deve_ter_entre_2_e_100_caracteres(self):
        param_list = [
            ('a'*1, False),
            ('a'*2, True),
            ('a'*100, True),
            ('a'*101, False),
        ]
        for params in param_list:
            with self.subTest(params):
                s = PescadorSerializer(data={'nome': 'Augusto', 'porto_desembarque_principal': self.porto.id, 'apelido': params[0]})
                self.assertEqual(s.is_valid(), params[1])

    def teste_data_nascimento_nao_pode_receber_blank(self):
        data = {
            'nome': 'João das Quantas',
            'porto_desembarque_principal': self.porto.id,
            'data_nascimento': '',
        }
        s = PescadorSerializer(data=data)
        self.assertFalse(s.is_valid())

    def teste_data_nascimento_pode_receber_none(self):
        data = {
            'nome': 'João das Quantas',
            'porto_desembarque_principal': self.porto.id,
            'data_nascimento': None,
        }
        s = PescadorSerializer(data=data)
        self.assertTrue(s.is_valid())

    def teste_cpf_deve_ter_11_caracteres_numericos(self):
        params_list = [
            (11122233344, True),
            ('12312312345', True),
            (111222333.44 , False),
            ('123aaa456bb', False),
            ('123456789012', False),
            ('1234567890', False),
        ]
        for params in params_list:
            with self.subTest(params):
                s = PescadorSerializer(data={'nome': 'Fulano', 'porto_desembarque_principal': self.porto.id, 'cpf': params[0]})
                self.assertEqual(s.is_valid(), params[1])

    def teste_renda_mensal_deve_ser_positiva(self):
        params_list = [
            (1000, True),
            (0, True),
            (-1000, False),
        ]
        for params in params_list:
            with self.subTest(params):
                s = PescadorSerializer(data={
                    'nome': 'Fulano',
                    'porto_desembarque_principal': self.porto.id,
                    'renda_mensal_pesca': params[0]
                })
                self.assertEqual(s.is_valid(), params[1])

    def teste_ativo_verdadeiro_por_default(self):
        s = PescadorSerializer(data={'nome': 'Fulano', 'porto_desembarque_principal': self.porto.id})
        s.is_valid()
        s.save()
        self.assertTrue(s.data['ativo'])
    
    def teste_falecido_falso_por_default(self):
        s = PescadorSerializer(data={'nome': 'Fulano', 'porto_desembarque_principal': self.porto.id})
        s.is_valid()
        s.save()
        self.assertFalse(s.data['falecido'])
