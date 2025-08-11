from rest_framework import serializers
from pescadores.models import MotivacaoPesca

class MotivacaoPescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivacaoPesca
        fields = ['id', 'descricao']
