from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import DestinoPescado
from pescadores.serializers import DestinoPescadoSerializer

class DestinoPescadoList(ListCreateAPIView):
    queryset = DestinoPescado.objects.all()
    serializer_class = DestinoPescadoSerializer

class DestinoPescadoDetail(RetrieveUpdateDestroyAPIView):
    queryset = DestinoPescado.objects.all()
    serializer_class = DestinoPescadoSerializer
