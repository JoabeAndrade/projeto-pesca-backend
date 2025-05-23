from rest_framework import generics
from pescadores.models import Associacao
from pescadores.serializers import AssociacaoSerializer

class AssociacaoList(generics.ListCreateAPIView):
    queryset = Associacao.objects.all()
    serializer_class = AssociacaoSerializer

class AssociacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Associacao.objects.all()
    serializer_class = AssociacaoSerializer
