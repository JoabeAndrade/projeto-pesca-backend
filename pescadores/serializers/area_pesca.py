from rest_framework import serializers
from pescadores.models import AreaPesca

class AreaPescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaPesca
        fields = ['id', 'descricao']
