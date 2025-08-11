from rest_framework import serializers
from pescadores.models import HorarioPesca

class HorarioPescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioPesca
        fields = ['id', 'descricao']
