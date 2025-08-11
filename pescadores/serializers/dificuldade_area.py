from rest_framework import serializers
from pescadores.models import DificuldadeArea

class DificuldadeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DificuldadeArea
        fields = ['id', 'descricao']
