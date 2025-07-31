from pescadores.models import ProgramaSocial
from pescadores.serializers import ProgramaSocialSerialzier
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

class ProgramaSocialListView(ListCreateAPIView):
    queryset = ProgramaSocial.objects.all()
    serializer_class = ProgramaSocialSerialzier

class ProgramaSocialDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ProgramaSocial.objects.all()
    serializer_class = ProgramaSocialSerialzier
