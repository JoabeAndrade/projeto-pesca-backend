from rest_framework import serializers
from pescadores.models import Associacao
from pescadores.serializers import EnderecoSerializer

class AssociacaoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Associacao
        fields = ['id', 'nome', 'endereco']
