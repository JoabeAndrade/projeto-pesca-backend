from rest_framework import serializers
from pescadores.models import FrequenciaPesca

class FrequenciaPescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequenciaPesca
        fields = ['id', 'descricao']
