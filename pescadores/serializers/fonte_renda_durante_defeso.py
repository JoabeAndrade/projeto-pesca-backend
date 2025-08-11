from rest_framework import serializers
from pescadores.models import FonteRendaDuranteDefeso

class FonteRendaDuranteDefesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FonteRendaDuranteDefeso
        fields = ['id', 'descricao']
