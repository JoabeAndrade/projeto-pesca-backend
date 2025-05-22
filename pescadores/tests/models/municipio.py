from django.test import TestCase
from django.core.exceptions import ValidationError
from pescadores.models import Municipio

class TestesMunicipio(TestCase):
    def teste_dados_validos(self):
        mun = Municipio(nome='Ilhéus', uf='BA')
        mun.full_clean()

    def teste_nome_obrigatorio(self):
        mun = Municipio(uf='BA')
        self.assertRaises(ValidationError, mun.full_clean)

    def teste_nome_tem_no_maximo_100_caracteres(self):
        mun1 = Municipio(nome='a' * 100, uf='PE')
        mun1.full_clean()
        mun2 = Municipio(nome='a' * 101, uf='PE')
        self.assertRaises(ValidationError, mun2.full_clean)

    def teste_uf_obrigatoria(self):
        mun = Municipio(nome='Ilhéus')
        self.assertRaises(ValidationError, mun.full_clean)

    def teste_uf_sigla_deve_estar_em_letras_maiusculas(self):
        mun = Municipio(nome='Ilhéus', uf='ba')
        self.assertRaises(ValidationError, mun.full_clean)

    def teste_par_nome_uf_unico(self):
        Municipio.objects.create(nome='Springfield', uf='BA')
        spring_ceara = Municipio(nome='Springfield', uf='CE')
        spring_bahia = Municipio(nome='Springfield', uf='BA')
        spring_ceara.full_clean()
        self.assertRaises(ValidationError, spring_bahia.full_clean)
