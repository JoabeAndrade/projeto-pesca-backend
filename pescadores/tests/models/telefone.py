from django.test import TestCase
from pescadores.models import Telefone
from django.core.exceptions import ValidationError
from unittest import skip
from pescadores.tests.utils import create_pescador_dados_validos

class TestesPescador(TestCase):
    def setUp(self):
        self.pescador = create_pescador_dados_validos()

    def teste_dados_validos(self):
        telefone = Telefone(numero='123456789', pescador=self.pescador)
        telefone.full_clean()
        telefone.save()

    def teste_numero_obrigatorio(self):
        telefone = Telefone(pescador=self.pescador)
        self.assertRaises(ValidationError, telefone.full_clean)

    def teste_numero_tem_no_maximo_20_caracteres(self):
        param_list = [
            ('', False),
            (None, False),
            ('1' * 20, True),
            ('1' * 21, False),
        ]
        for params in param_list:
            with self.subTest(params):
                telefone = Telefone(numero=params[0], pescador=self.pescador)
                if params[1]:
                    telefone.full_clean()
                else:
                    self.assertRaises(ValidationError, telefone.full_clean)

    def teste_numero_caracteres_sao_todos_numericos(self):
        param_list = [
            ('123456789', True),
            ('12345-6789', False),
            ('abcdefghi', False),
            ('123a56789', False),
            (123456789, True),
        ]
        for params in param_list:
            with self.subTest(params):
                telefone = Telefone(numero=params[0], pescador=self.pescador)
                if params[1]:
                    telefone.full_clean()
                else:
                    self.assertRaises(ValidationError, telefone.full_clean)

    def teste_pescador_obrigatorio(self):
        telefone = Telefone(numero='123456789')
        self.assertRaises(ValidationError, telefone.full_clean)

    @skip
    def teste_apagar_pescador_apaga_os_telefones(self):
        t1 = Telefone.objects.create(numero='123456789', pescador=self.pescador)
        t2 = Telefone.objects.create(numero='321654987', pescador=self.pescador)
        assert t1.id == 1
        assert t2.id == 2
        self.pescador.delete()
        self.assertIsNone(t1.id)
        self.assertIsNone(t2.id)
