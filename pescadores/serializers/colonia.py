from rest_framework import serializers
from pescadores.models import Colonia, Comunidade, Endereco
from .comunidade import ComunidadeSerializer
from .endereco import EnderecoSerializer

class ColoniaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer(read_only=True)
    comunidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Comunidade.objects.all(),
        source='comunidade',
        write_only=True
    )
    endereco_sede = EnderecoSerializer(read_only=True)
    endereco_sede_id = serializers.PrimaryKeyRelatedField(
        queryset=Endereco.objects.all(),
        source='endereco_sede',
        write_only=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Colonia
        fields = [
            'id',
            'codigo',
            'comunidade',
            'comunidade_id',
            'endereco_sede',
            'endereco_sede_id',
        ]
