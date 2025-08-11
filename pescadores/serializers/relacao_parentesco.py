from rest_framework import serializers
from pescadores.models import RelacaoParentesco

class RelacaoParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacaoParentesco
        fields = ['id', 'descricao']
