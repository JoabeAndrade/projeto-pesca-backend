from rest_framework import serializers
from pescadores.models import Pescador, Municipio, Colonia, Comunidade
from .municipio import MunicipioSerializer
from .colonia import ColoniaSerializer
from .comunidade import ComunidadeSerializer
from .endereco import EnderecoSerializer
from .dependente import DependenteSerializer
from .telefone import TelefoneSerializer

class PescadorSerializer(serializers.ModelSerializer):
    naturalidade = MunicipioSerializer(read_only=True)
    naturalidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipio.objects.all(),
        source='naturalidade',
        write_only=True,
        required=False,
    )
    colonia = ColoniaSerializer(read_only=True)
    colonia_id = serializers.PrimaryKeyRelatedField(
        queryset=Colonia.objects.all(),
        source='colonia',
        write_only=True,
        required=False,
    )
    comunidade = ComunidadeSerializer(read_only=True)
    comunidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Comunidade.objects.all(),
        source='comunidade',
        write_only=True,
        required=False,
    )
    enderecos = EnderecoSerializer(many=True, read_only=True)
    dependentes = DependenteSerializer(many=True, read_only=True)
    telefones = TelefoneSerializer(many=True, read_only=True)

    class Meta:
        model = Pescador
        fields = [
            'id',
            'nome',
            'sexo',
            'apelido',
            'naturalidade',
            'naturalidade_id',
            'data_nascimento',
            'nome_pai',
            'nome_mae',
            'colonia',
            'colonia_id',
            'matricula_colonia',
            'data_inscricao_colonia',
            'comunidade',
            'comunidade_id',
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
