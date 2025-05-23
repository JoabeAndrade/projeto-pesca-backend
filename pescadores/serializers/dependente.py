from rest_framework import serializers
from pescadores.models import Dependente

class DependenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependente
        fields = ['id', 'relacao', 'quantidade', 'pescador']
        extra_kwargs = {
            'id': {'read_only': True},
            'relacao': {'required': True, 'allow_null': False},
            'quantidade': {'required': True, 'allow_null': False},
            'pescador': {'required': True, 'write_only': True},
        }
