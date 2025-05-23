from pescadores.models import Endereco
from rest_framework import serializers

class EnderecoSerializer(serializers.ModelSerializer):
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
        ]
