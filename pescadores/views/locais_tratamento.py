from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import LocalTratamento
from pescadores.serializers import LocalTratamentoSerializer

class LocalTratamentoList(ListCreateAPIView):
    queryset = LocalTratamento.objects.all()
    serializer_class = LocalTratamentoSerializer

class LocalTratamentoDetail(RetrieveUpdateDestroyAPIView):
    queryset = LocalTratamento.objects.all()
    serializer_class = LocalTratamentoSerializer
