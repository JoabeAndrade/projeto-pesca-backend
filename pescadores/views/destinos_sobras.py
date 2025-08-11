from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import DestinoSobras
from pescadores.serializers import DestinoSobrasSerializer

class DestinoSobrasList(ListCreateAPIView):
    queryset = DestinoSobras.objects.all()
    serializer_class = DestinoSobrasSerializer

class DestinoSobrasDetail(RetrieveUpdateDestroyAPIView):
    queryset = DestinoSobras.objects.all()
    serializer_class = DestinoSobrasSerializer
