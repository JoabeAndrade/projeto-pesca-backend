from pescadores.models import ProgramaSocial
from pescadores.serializers import ProgramaSocialSerialzier
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

class ProgramaSocialList(ListCreateAPIView):
    queryset = ProgramaSocial.objects.all()
    serializer_class = ProgramaSocialSerialzier

class ProgramaSocialDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProgramaSocial.objects.all()
    serializer_class = ProgramaSocialSerialzier
