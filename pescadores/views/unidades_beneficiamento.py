from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import UnidadeBeneficiamento
from pescadores.serializers import UnidadeBeneficiamentoSerializer

class UnidadeBeneficiamentoList(ListCreateAPIView):
    queryset = UnidadeBeneficiamento.objects.all()
    serializer_class = UnidadeBeneficiamentoSerializer

class UnidadeBeneficiamentoDetail(RetrieveUpdateDestroyAPIView):
    queryset = UnidadeBeneficiamento.objects.all()
    serializer_class = UnidadeBeneficiamentoSerializer
