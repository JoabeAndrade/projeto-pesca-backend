from rest_framework import serializers
from pescadores.models import EmissorRgp

class EmissorRgpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissorRgp
        fields = ['id', 'nome']
