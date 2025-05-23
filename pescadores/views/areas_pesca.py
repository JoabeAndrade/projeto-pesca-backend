from rest_framework import generics
from pescadores.models import AreaPesca
from pescadores.serializers import AreaPescaSerializer

class AreaPescaList(generics.ListCreateAPIView):
    queryset = AreaPesca.objects.all()
    serializer_class = AreaPescaSerializer

class AreaPescaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaPesca.objects.all()
    serializer_class = AreaPescaSerializer
