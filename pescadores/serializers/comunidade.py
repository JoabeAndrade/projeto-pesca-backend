from rest_framework import serializers
from pescadores.models import Comunidade, Municipio
from .municipio import MunicipioSerializer

class ComunidadeSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer(read_only=True)
    municipio_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipio.objects.all(),
        source='municipio',
        write_only=True
    )

    class Meta:
        model = Comunidade
        fields = [
            'id',
            'nome',
            'municipio',
            'municipio_id',
        ]
