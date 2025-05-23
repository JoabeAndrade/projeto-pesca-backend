from rest_framework import generics
from pescadores.models import ArtePesca
from pescadores.serializers import ArtePescaSerializer

class ArtePescaList(generics.ListCreateAPIView):
    queryset = ArtePesca.objects.all()
    serializer_class = ArtePescaSerializer

class ArtePescaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtePesca.objects.all()
    serializer_class = ArtePescaSerializer
