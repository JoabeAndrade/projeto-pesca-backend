from rest_framework import serializers
from pescadores.models import AtividadeAnterior

class AtividadeAnteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeAnterior
        fields = ['id', 'descricao']
