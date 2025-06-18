from rest_framework import serializers
from pescadores.models import Colonia, Comunidade
from .comunidade import ComunidadeSerializer
from .endereco import EnderecoSerializer

class ColoniaSerializer(serializers.ModelSerializer):
    comunidade = ComunidadeSerializer(read_only=True)
    comunidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Comunidade.objects.all(),
        source='comunidade',
        write_only=True
    )
    endereco_sede = EnderecoSerializer()

    class Meta:
        model = Colonia
        fields = [
            'id',
            'codigo',
            'comunidade',
            'comunidade_id',
            'endereco_sede',
        ]
