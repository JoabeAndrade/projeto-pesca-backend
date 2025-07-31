from rest_framework import serializers
from pescadores.models import Pescador, Municipio, Colonia, Comunidade, Endereco
from .municipio import MunicipioSerializer
from .colonia import ColoniaSerializer
from .comunidade import ComunidadeSerializer
from .endereco import EnderecoSerializer
from .dependente import DependenteSerializer
from .telefone import TelefoneSerializer
from .area_pesca import AreaPescaSerializer
from .arte_pesca import ArtePescaSerializer
from .associacao import AssociacaoSerializer

class PescadorSerializer(serializers.ModelSerializer):
    naturalidade = MunicipioSerializer(read_only=True)
    naturalidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipio.objects.all(),
        source='naturalidade',
        write_only=True,
        allow_null=True,
        required=False,
    )
    colonia = ColoniaSerializer(read_only=True)
    colonia_id = serializers.PrimaryKeyRelatedField(
        queryset=Colonia.objects.all(),
        source='colonia',
        write_only=True,
        allow_null=True,
        required=False,
    )
    comunidade = ComunidadeSerializer(read_only=True)
    comunidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Comunidade.objects.all(),
        source='comunidade',
        write_only=True,
        allow_null=True,
        required=False,
    )
    endereco = EnderecoSerializer(read_only=True)
    endereco_id = serializers.PrimaryKeyRelatedField(
        queryset=Endereco.objects.all(),
        source='endereco',
        write_only=True,
        allow_null=True,
        required=False,
    )
    dependentes = DependenteSerializer(many=True, read_only=True)
    telefones = TelefoneSerializer(many=True, read_only=True)
    artes_pesca = ArtePescaSerializer(many=True, read_only=True)
    areas_pesca = AreaPescaSerializer(many=True, read_only=True)
    associacoes = AssociacaoSerializer(many=True, read_only=True)

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
            'falecido',
            'data_cadastramento',
            'endereco',
            'endereco_id',
            'dependentes',
            'telefones',
            'artes_pesca',
            'areas_pesca',
            'associacoes',
            'porto_desembarque_principal',
            'programas_sociais',
            'projeto',
        ]
        extra_kwargs = {
            'programas_sociais': {
                'allow_empty': True,
                'required': False,
            },
        }
