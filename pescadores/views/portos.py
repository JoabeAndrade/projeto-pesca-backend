from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import Porto
from pescadores.serializers import PortoSerializer

class PortoList(ListCreateAPIView):
    queryset = Porto.objects.all()
    serializer_class = PortoSerializer

class PortoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Porto.objects.all()
    serializer_class = PortoSerializer
