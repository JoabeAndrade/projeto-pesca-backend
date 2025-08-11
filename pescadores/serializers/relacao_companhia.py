from rest_framework import serializers
from pescadores.models import RelacaoCompanhia

class RelacaoCompanhiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacaoCompanhia
        fields = ['id', 'descricao']
