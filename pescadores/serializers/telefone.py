from rest_framework import serializers
from pescadores.models import Telefone

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['id', 'pescador', 'numero']
        extra_kwargs = {
            'id': {'read_only': True},
            'pescador': {'required': True, 'write_only': True, 'allow_null': False},
            'numero': {'required': True, 'allow_null': False},
        }
