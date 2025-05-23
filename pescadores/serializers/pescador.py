from rest_framework import serializers
from pescadores.models import Pescador
from .municipio import MunicipioSerializer
from .colonia import ColoniaSerializer
from .endereco import EnderecoSerializer
from .dependente import DependenteSerializer
from .telefone import TelefoneSerializer

class PescadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pescador
        fields = [
            'id',
            'nome',
            'sexo',
            'apelido',
            'naturalidade',
            'cidade_natal',
            'data_nascimento',
            'nome_pai',
            'nome_mae',
            'colonia',
            'colonia_inscrita',
            'matricula_colonia',
            'data_inscricao_colonia',
            'rg',
            'cpf',
            'tipo_embarcacao',
            'tamanho_embarcacao',
            'proprietario_embarcacao',
            'escolaridade',
            'renda_mensal_pesca',
            'outra_renda',
            'ativo',
            'motivo_inatividade',
            'telefones',
            'falecido',
            'data_cadastramento',
            'enderecos',
            'dependentes',
            'telefones',
        ]
        extra_kwargs = {
            'naturalidade': {'write_only': True},
            'colonia': {'write_only': True},
        }

    cidade_natal = MunicipioSerializer(source='naturalidade', read_only=True)
    colonia_inscrita = ColoniaSerializer(source='colonia', read_only=True)
    enderecos = EnderecoSerializer(many=True, read_only=True)
    dependentes = DependenteSerializer(many=True, read_only=True)
    telefones = TelefoneSerializer(many=True, read_only=True)
