from rest_framework import serializers
from pescadores.models import CursoBeneficiamento

class CursoBeneficiamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoBeneficiamento
        fields = ['id', 'nome']
