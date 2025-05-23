from rest_framework import generics
from pescadores.models import Comunidade
from pescadores.serializers import ComunidadeSerializer

class ComunidadeList(generics.ListCreateAPIView):
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer

class ComunidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer
