from rest_framework.serializers import ModelSerializer
from pescadores.models import ProgramaSocial

class ProgramaSocialSerialzier(ModelSerializer):
    class Meta:
        model = ProgramaSocial
        fields = ['id', 'nome']
