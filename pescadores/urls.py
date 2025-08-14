from django.urls import path
from pescadores import views

urlpatterns = [
    path(
        'areaspesca/',
        views.AreaPescaList.as_view(),
        name='area_pesca_list',
    ),
    path(
        'areaspesca/<int:pk>/', # <-- Corrigido
        views.AreaPescaDetail.as_view(),
        name='area_pesca_detail',
    ),
    path(
        'artespesca/',
        views.ArtePescaList.as_view(),
        name='arte_pesca_list',
    ),
    path(
        'artespesca/<int:pk>/', # <-- Corrigido
        views.ArtePescaDetail.as_view(),
        name='arte_pesca_detail',
    ),
    path(
        'associacoes/',
        views.AssociacaoList.as_view(),
        name='associacao_list',
    ),
    path(
        'associacoes/<int:pk>/', # <-- Corrigido
        views.AssociacaoDetail.as_view(),
        name='associacao_detail',
    ),
    path(
        'atividadesanteriores/',
        views.AtividadeAnteriorList.as_view(),
        name='atividade_anterior_list',
    ),
    path(
        'atividadesanteriores/<int:pk>/', # <-- Corrigido
        views.AtividadeAnteriorDetail.as_view(),
        name='atividade_anterior_detail',
    ),
    path(
        'colonias/',
        views.ColoniaList.as_view(),
        name='colonia_list',
    ),
    path(
        'colonias/<int:pk>/', # <-- Corrigido
        views.ColoniaDetail.as_view(),
        name='colonia_detail',
    ),
    path(
        'compradorespescado/',
        views.CompradorPescadoList.as_view(),
        name='comprador_pescado_list',
    ),
    path(
        'compradorespescado/<int:pk>/', # <-- Corrigido
        views.CompradorPescadoDetail.as_view(),
        name='comprador_pescado_detail',
    ),
    path(
        'comunidades/',
        views.ComunidadeList.as_view(),
        name='comunidade_list',
    ),
    path(
        'comunidades/<int:pk>/', # <-- Corrigido
        views.ComunidadeDetail.as_view(),
        name='comunidade_detail',
    ),
    path(
        'dependentes/',
        views.DependenteView.as_view(),
        name='dependente_list',
    ),
    path(
        'dependentes/<int:pk>/', # <-- Corrigido
        views.DependenteView.as_view(),
        name='dependente_detail',
    ),
    path(
        'enderecos/',
        views.EnderecoList.as_view(),
        name='endereco_list',
    ),
    path(
        'enderecos/<int:pk>/', # <-- Corrigido
        views.EnderecoDetail.as_view(),
        name='endereco_detail',
    ),
    path(
        'municipios/',
        views.MunicipioList.as_view(),
        name='municipio_list',
    ),
    path(
        'municipios/<int:pk>/', # <-- Corrigido
        views.MunicipioDetail.as_view(),
        name='municipio_detail',
    ),
    path(
        'especialistas/',
        views.PescadorEspecialistaList.as_view(),
        name='especialista_list',
    ),
    path(
        'especialistas/<int:pk>/', # <-- Corrigido
        views.PescadorEspecialistaDetail.as_view(),
        name='especialista_detail',
    ),
    path(
        'pescadores/',
        views.PescadorList.as_view(),
        name='pescador_list',
    ),
    path(
        'pescadores/<int:pk>/', # <-- Corrigido
        views.PescadorDetail.as_view(),
        name='pescador_detail',
    ),
    path(
        'pescadores/<int:pk_pescador>/areaspesca/', # <-- Corrigido
        views.AreasPescaDoPescadorView.as_view(),
    ),
    path(
        'pescadores/<int:pk_pescador>/artespesca/', # <-- Corrigido
        views.ArtesPescaDoPescadorView.as_view(),
    ),
    path(
        'pescadores/<int:pk_pescador>/associacoes/', # <-- Corrigido
        views.AssociacoesDoPescadorView.as_view(),
    ),
    path(
        'portos/',
        views.PortoList.as_view(),
        name='porto_list',
    ),
    path(
        'portos/<int:pk>/', # <-- Corrigido
        views.PortoDetail.as_view(),
        name='porto_detail',
    ),
    path(
        'programas/',
        views.ProgramaSocialList.as_view(),
        name='programa_list',
    ),
    path(
        'programas/<int:pk>/', # <-- Corrigido
        views.ProgramaSocialDetail.as_view(),
        name='programa_detail',
    ),
    path(
        'projetos/',
        views.ProjetoList.as_view(),
        name='projeto_list',
    ),
    path(
        'projetos/<int:pk>/', # <-- Corrigido
        views.ProjetoDetail.as_view(),
        name='projeto_detail',
    ),
    path(
        'telefones/',
        views.TelefoneList.as_view(),
        name='telefone_list',
    ),
    path(
        'telefones/<int:pk>/', # <-- Corrigido
        views.TelefoneDetail.as_view(),
        name='telefone_detail',
    ),
]