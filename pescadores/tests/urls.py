from django.test import TestCase
from django.urls import reverse

class TesteUrls(TestCase):
    def teste_url_area_pesca_list(self):
        url = reverse('area_pesca_list')
        assert url == '/areaspesca/'

    def teste_url_area_pesca_detail(self):
        url = reverse('area_pesca_detail', kwargs={'pk': 1})
        assert url == '/areaspesca/1'

    def teste_url_arte_pesca_list(self):
        url = reverse('arte_pesca_list')
        assert url == '/artespesca/'

    def teste_url_arte_pesca_detail(self):
        url = reverse('arte_pesca_detail', kwargs={'pk': 1})
        assert url == '/artespesca/1'

    def teste_url_associacao_list(self):
        url = reverse('associacao_list')
        assert url == '/associacoes/'

    def teste_url_associacao_list(self):
        url = reverse('associacao_detail', kwargs={'pk': 1})
        assert url == '/associacoes/1'

    def teste_url_colonia_list(self):
        url = reverse('colonia_list')
        assert url == '/colonias/'

    def teste_url_colonia_detail(self):
        url = reverse('colonia_detail', kwargs={'pk': 1})
        assert url == '/colonias/1'

    def teste_url_comunidade_list(self):
        url = reverse('comunidade_list')
        assert url == '/comunidades/'
    
    def teste_url_comunidade_detail(self):
        url = reverse('comunidade_detail', kwargs={'pk': 1})
        assert url == '/comunidades/1'

    def teste_url_dependente_list(self):
        url = reverse('dependente_list')
        assert url == '/dependentes/'
    
    def teste_url_dependente_detail(self):
        url = reverse('dependente_detail', kwargs={'pk': 1})
        assert url == '/dependentes/1'

    def teste_url_endereco_list(self):
        url = reverse('endereco_list')
        assert url == '/enderecos/'

    def teste_url_endereco_detail(self):
        url = reverse('endereco_detail', kwargs={'pk': 1})
        assert url == '/enderecos/1'
    
    def teste_url_municipio_list(self):
        url = reverse('municipio_list')
        assert url == '/municipios/'

    def teste_url_municipio_detail(self):
        url = reverse('municipio_detail', kwargs={'pk': 1})
        assert url == '/municipios/1'

    def teste_url_pescador_list(self):
        url = reverse('pescador_list')
        assert url == '/pescadores/'

    def teste_url_pescador_detail(self):
        url = reverse('pescador_detail', kwargs={'pk': 1})
        assert url == '/pescadores/1'
