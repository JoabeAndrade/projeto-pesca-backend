from rest_framework import serializers
from pescadores.models import CompradorPescado

class CompradorPescadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompradorPescado
        fields = ['id', 'descricao']
