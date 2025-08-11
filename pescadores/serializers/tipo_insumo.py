from rest_framework import serializers
from pescadores.models import TipoInsumo

class TipoInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInsumo
        fields = ['id', 'descricao']
