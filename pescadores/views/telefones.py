from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import Telefone
from pescadores.serializers import TelefoneSerializer

class TelefoneList(ListCreateAPIView):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer

class TelefoneDetail(RetrieveUpdateDestroyAPIView):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
