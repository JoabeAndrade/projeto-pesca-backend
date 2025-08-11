from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import AtividadeAnterior
from pescadores.serializers import AtividadeAnteriorSerializer

class AtividadeAnteriorList(ListCreateAPIView):
    queryset = AtividadeAnterior.objects.all()
    serializer_class = AtividadeAnteriorSerializer

class AtividadeAnteriorDetail(RetrieveUpdateDestroyAPIView):
    queryset = AtividadeAnterior.objects.all()
    serializer_class = AtividadeAnteriorSerializer
