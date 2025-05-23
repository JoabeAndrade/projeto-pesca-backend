from rest_framework import serializers
from pescadores.models import ArtePesca

class ArtePescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtePesca
        fields = ['id', 'nome']
