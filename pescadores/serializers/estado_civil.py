from rest_framework import serializers
from pescadores.models import EstadoCivil

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = ['id', 'descricao']
