from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import Projeto
from pescadores.serializers import ProjetoSerializer

class ProjetoList(ListCreateAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class ProjetoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
