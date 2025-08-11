from rest_framework import serializers
from pescadores.models import InsumoDoPescador

class InsumoDoPescadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsumoDoPescador
        fields = ['id', 'tipo', 'valor', 'pescador_especialista']
