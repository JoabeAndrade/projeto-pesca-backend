from rest_framework import serializers
from pescadores.models import Comunidade

class ComunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidade
        fields = ['id', 'nome', 'municipio']
