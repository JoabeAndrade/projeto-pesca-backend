from rest_framework import serializers
from pescadores.models import TipoResidencia

class TipoResidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResidencia
        fields = ['id', 'descricao']
