from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import Endereco
from pescadores.serializers import EnderecoSerializer

class EnderecoList(ListCreateAPIView):
    queryset = Endereco.objects.all().select_related('municipio')
    serializer_class = EnderecoSerializer

class EnderecoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
