from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import CursoBeneficiamento
from pescadores.serializers import CursoBeneficiamentoSerializer

class CursoBeneficiamentoList(ListCreateAPIView):
    queryset = CursoBeneficiamento.objects.all()
    serializer_class = CursoBeneficiamentoSerializer

class CursoBeneficiamentoDetail(RetrieveUpdateDestroyAPIView):
    queryset = CursoBeneficiamento.objects.all()
    serializer_class = CursoBeneficiamentoSerializer
