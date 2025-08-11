from rest_framework import serializers
from pescadores.models import DestinoSobras

class DestinoSobrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinoSobras
        fields = ['id', 'descricao']
