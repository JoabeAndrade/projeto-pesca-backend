from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import FrequenciaConsumo
from pescadores.serializers import FrequenciaConsumoSerializer

class FrequenciaConsumoList(ListCreateAPIView):
    queryset = FrequenciaConsumo.objects.all()
    serializer_class = FrequenciaConsumoSerializer

class FrequenciaConsumoDetail(RetrieveUpdateDestroyAPIView):
    queryset = FrequenciaConsumo.objects.all()
    serializer_class = FrequenciaConsumoSerializer
