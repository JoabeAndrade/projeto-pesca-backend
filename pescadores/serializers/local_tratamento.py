from rest_framework import serializers
from pescadores.models import LocalTratamento

class LocalTratamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalTratamento
        fields = ['id', 'descricao']
