from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import MotivacaoPesca
from pescadores.serializers import MotivacaoPescaSerializer

class MotivacaoPescaList(ListCreateAPIView):
    queryset = MotivacaoPesca.objects.all()
    serializer_class = MotivacaoPescaSerializer

class MotivacaoPescaDetail(RetrieveUpdateDestroyAPIView):
    queryset = MotivacaoPesca.objects.all()
    serializer_class = MotivacaoPescaSerializer
