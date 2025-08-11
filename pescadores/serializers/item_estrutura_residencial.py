from rest_framework import serializers
from pescadores.models import ItemEstruturaResidencial

class ItemEstruturaResidencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEstruturaResidencial
        fields = ['id', 'descricao']
