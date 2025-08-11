from rest_framework import serializers
from pescadores.models import TipoSeguroDefeso

class TipoSeguroDefesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSeguroDefeso
        fields = ['id', 'nome']
