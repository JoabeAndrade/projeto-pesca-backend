from rest_framework import serializers
from pescadores.models import DestinoPescado

class DestinoPescadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinoPescado
        fields = ['id', 'descricao']
