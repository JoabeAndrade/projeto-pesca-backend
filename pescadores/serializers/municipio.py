from rest_framework import serializers
from pescadores.models import Municipio

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id', 'nome', 'uf']
