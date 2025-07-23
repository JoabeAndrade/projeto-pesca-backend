from rest_framework import serializers
from pescadores.models import Porto, Municipio
from pescadores.serializers import MunicipioSerializer

class PortoSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer(read_only=True)
    municipio_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipio.objects.all(),
        source='municipio',
        write_only=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Porto
        fields = ['id', 'nome', 'municipio_id', 'municipio']
