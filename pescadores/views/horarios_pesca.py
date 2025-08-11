from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import HorarioPesca
from pescadores.serializers import HorarioPescaSerializer

class HorarioPescaList(ListCreateAPIView):
    queryset = HorarioPesca.objects.all()
    serializer_class = HorarioPescaSerializer

class HorarioPescaDetail(RetrieveUpdateDestroyAPIView):
    queryset = HorarioPesca.objects.all()
    serializer_class = HorarioPescaSerializer
