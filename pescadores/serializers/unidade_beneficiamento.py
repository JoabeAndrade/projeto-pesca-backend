from rest_framework import serializers
from pescadores.models import UnidadeBeneficiamento

class UnidadeBeneficiamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeBeneficiamento
        fields = ['id', 'nome']
