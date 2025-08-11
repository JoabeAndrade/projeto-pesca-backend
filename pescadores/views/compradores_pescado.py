from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import CompradorPescado
from pescadores.serializers import CompradorPescadoSerializer

class CompradorPescadoList(ListCreateAPIView):
    queryset = CompradorPescado.objects.all()
    serializer_class = CompradorPescadoSerializer

class CompradorPescadoDetail(RetrieveUpdateDestroyAPIView):
    queryset = CompradorPescado.objects.all()
    serializer_class = CompradorPescadoSerializer
