from rest_framework import serializers
from pescadores.models import FrequenciaConsumo

class FrequenciaConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequenciaConsumo
        fields = ['id', 'descricao']
