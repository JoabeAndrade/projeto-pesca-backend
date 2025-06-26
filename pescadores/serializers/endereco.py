from rest_framework import serializers
from pescadores.models import Endereco, Municipio
from .municipio import MunicipioSerializer

class EnderecoSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer(read_only=True)
    municipio_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipio.objects.all(),
        source='municipio',
        write_only=True
    )

    class Meta:
        model = Endereco
        fields = [
            'id',
            'logradouro',
            'numero',
            'bairro',
            'cep',
            'complemento',
            'municipio',
            'municipio_id',
        ]
