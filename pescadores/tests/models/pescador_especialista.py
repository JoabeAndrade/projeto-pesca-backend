from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from pescadores.models import (
    PescadorEspecialista,
    Pescador,
    EstadoCivil,
    TipoResidencia,
    AtividadeAnterior,
)
from pescadores.tests.utils import create_pescador_dados_validos

class TestePescadorEspecialista(TestCase):
    def teste_dados_validos(self):
        p = create_pescador_dados_validos()
        c = EstadoCivil.objects.create(descricao='Solteiro(a)')
        tr = TipoResidencia.objects.create(descricao='Própria')
        aa = AtividadeAnterior.objects.create(descricao='Comerciante')
        e = PescadorEspecialista(
            pescador=p,
            estado_civil=c,
            quantidade_filhos=2,
            reside_no_municipio=True,
            desde_quando_reside_no_municipio="2005-05-05",
            tipo_de_residencia=tr,
            quantidade_moradores_na_casa=5,
            estacao_maior_renda='v',
            valor_maior_renda="1555.55",
            estacao_menor_renda='i',
            valor_menor_renda="599.99",
            quando_comecou="2015-10-10",
            atividade_anterior=aa,
            duracao_pescaria_dias=2,
            duracao_pescaria_horas=8,
            possui_rgp=True,
        )
        e.full_clean()
        e.save()

    def teste_pescador_obrigatorio(self):
        especialista = PescadorEspecialista()
        with self.assertRaises(ValidationError):
            especialista.full_clean()

    def teste_outros_atributos_sao_opcionais(self):
        pescador = create_pescador_dados_validos()
        especialista = PescadorEspecialista(pescador=pescador)
        especialista.full_clean()
        especialista.save()

    def teste_pescador_nao_pode_ter_mais_de_um_registro_de_especialista(self):
        p = create_pescador_dados_validos()
        PescadorEspecialista.objects.create(pescador=p)
        e2 = PescadorEspecialista(pescador=p)
        self.assertRaises(ValidationError, e2.full_clean)

    def teste_pescador_com_dados_especialista_nao_pode_ser_excluido(self):
        p = create_pescador_dados_validos()
        PescadorEspecialista.objects.create(pescador=p)
        self.assertRaises(ProtectedError, p.delete)

    def teste_quantidade_filhos_nao_pode_ser_negativa(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, quantidade_filhos=-1)
        self.assertRaises(ValidationError, e.full_clean)

    def teste_quantidade_filhos_blank_diferente_de_zero(self):
        p1 = create_pescador_dados_validos()
        p2 = create_pescador_dados_validos(nome='José')
        e1 = PescadorEspecialista.objects.create(pescador=p1)
        e2 = PescadorEspecialista.objects.create(pescador=p2, quantidade_filhos=0)
        self.assertIsNone(e1.quantidade_filhos)
        self.assertIsNotNone(e2.quantidade_filhos)
        self.assertEqual(e2.quantidade_filhos, 0)

    def teste_quantidade_moradores_na_casa_nao_pode_ser_negativa(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, quantidade_moradores_na_casa=-1)
        self.assertRaises(ValidationError, e.full_clean)

    def teste_quantidade_moradores_na_casa_blank_diferente_de_zero(self):
        p1 = create_pescador_dados_validos()
        p2 = create_pescador_dados_validos(nome='José')
        e1 = PescadorEspecialista.objects.create(pescador=p1)
        e2 = PescadorEspecialista.objects.create(pescador=p2, quantidade_moradores_na_casa=0)
        self.assertEqual(e1.quantidade_moradores_na_casa, None)
        self.assertEqual(e2.quantidade_moradores_na_casa, 0)

    def teste_valor_maior_renda_nao_pode_ser_negativa(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, valor_maior_renda="-1000")
        self.assertRaises(ValidationError, e.full_clean)

    def teste_valor_maior_renda_pode_ser_zero(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, valor_maior_renda="0")
        e.full_clean()
    
    def teste_valor_maior_renda_guarda_no_maximo_2_digitos_decimais(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, valor_maior_renda="533.333")
        self.assertRaises(ValidationError, e.full_clean)

    def teste_valor_menor_renda_nao_pode_ser_negativa(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, valor_menor_renda="-500")
        self.assertRaises(ValidationError, e.full_clean)

    def teste_valor_menor_renda_pode_ser_zero(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, valor_menor_renda="0")
        e.full_clean()

    def teste_valor_menor_renda_guarda_no_maximo_2_digitos_decimais(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, valor_menor_renda="199.999")
        self.assertRaises(ValidationError, e.full_clean)
    
    def teste_duracao_da_pescaria_em_dias_nao_pode_ser_negativa(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, duracao_pescaria_dias=-1)
        self.assertRaises(ValidationError, e.full_clean)

    def teste_duracao_da_pescaria_em_dias_pode_ser_zero(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, duracao_pescaria_dias=0)
        e.full_clean()
        e.save()

    def teste_duracao_da_pescaria_em_horas_nao_pode_ser_negativa(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, duracao_pescaria_horas=-1)
        self.assertRaises(ValidationError, e.full_clean)

    def teste_duracao_da_pescaria_em_horas_pode_ser_zero(self):
        p = create_pescador_dados_validos()
        e = PescadorEspecialista(pescador=p, duracao_pescaria_horas=0)
        e.full_clean()
        e.save()

    def create_pescador(self, nome='João'):
        return Pescador.objects.create(nome=nome)
