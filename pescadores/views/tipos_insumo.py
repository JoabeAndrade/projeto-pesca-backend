from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import TipoInsumo
from pescadores.serializers import TipoInsumoSerializer

class TipoInsumoList(ListCreateAPIView):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer

class TipoInsumoDetail(RetrieveUpdateDestroyAPIView):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer
