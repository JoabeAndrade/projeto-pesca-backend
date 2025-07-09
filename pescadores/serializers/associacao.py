from rest_framework import serializers
from pescadores.models import Associacao, Endereco
from pescadores.serializers import EnderecoSerializer

class AssociacaoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    endereco_id = serializers.PrimaryKeyRelatedField(
        queryset=Endereco.objects.all(),
        source='endereco',
        write_only=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Associacao
        fields = ['id', 'nome', 'endereco', 'endereco_id']
