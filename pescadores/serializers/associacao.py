from rest_framework import serializers
from pescadores.models import Associacao

class AssociacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associacao
        fields = ['id', 'nome', 'endereco']
