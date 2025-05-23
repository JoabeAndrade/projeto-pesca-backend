from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import Pescador
from pescadores.serializers import PescadorSerializer

class PescadorList(ListCreateAPIView):
    queryset = Pescador.objects.all()
    serializer_class = PescadorSerializer

class PescadorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pescador.objects.all()
    serializer_class = PescadorSerializer
