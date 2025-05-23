from rest_framework import serializers
from pescadores.models import Colonia

class ColoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colonia
        fields = ['id', 'codigo', 'endereco_sede']
