from rest_framework import generics
from pescadores.models import DificuldadeArea
from pescadores.serializers import DificuldadeAreaSerializer

class DificuldadeAreaList(generics.ListCreateAPIView):
    queryset = DificuldadeArea.objects.all()
    serializer_class = DificuldadeAreaSerializer

class DificuldadeAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DificuldadeArea.objects.all()
    serializer_class = DificuldadeAreaSerializer
