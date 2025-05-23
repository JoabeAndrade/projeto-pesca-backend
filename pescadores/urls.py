from django.urls import path
from pescadores import views

urlpatterns = [
    path('pescadores/', views.PescadorList.as_view(), name='pescador_list'),
    path('pescadores/<int:pk>', views.PescadorDetail.as_view(), name='pescador_detail'),
    path('dependentes/', views.DependenteView.as_view(), name='dependente_list'),
    path('dependentes/<int:pk>', views.DependenteView.as_view(), name='dependente_detail'),
    path('telefones/', views.TelefoneList.as_view()),
    path('telefones/<int:pk>', views.TelefoneDetail.as_view()),
    path('areaspesca/', views.AreaPescaList.as_view(), name='area_pesca_list'),
    path('areaspesca/<int:pk>', views.AreaPescaDetail.as_view(), name='area_pesca_detail'),
    path('artespesca/', views.ArtePescaList.as_view(), name='arte_pesca_list'),
    path('artespesca/<int:pk>', views.ArtePescaDetail.as_view(), name='arte_pesca_detail'),
    path('colonias/', views.ColoniaList.as_view(), name='colonia_list'),
    path('colonias/<int:pk>', views.ColoniaDetail.as_view(), name='colonia_detail'),
    path('municipios/', views.MunicipioList.as_view(), name='municipio_list'),
    path('municipios/<int:pk>', views.MunicipioDetail.as_view(), name='municipio_detail'),
    path('enderecos/', views.EnderecoList.as_view(), name='endereco_list'),
    path('enderecos/<int:pk>', views.EnderecoDetail.as_view(), name='endereco_detail'),
    path('associacoes/', views.AssociacaoList.as_view(), name='associacao_list'),
    path('associacoes/<int:pk>', views.AssociacaoDetail.as_view(), name='associacao_detail'),
    path('comunidades/', views.ComunidadeList.as_view(), name='comunidade_list'),
    path('comunidades/<int:pk>', views.ComunidadeDetail.as_view(), name='comunidade_detail'),
]
