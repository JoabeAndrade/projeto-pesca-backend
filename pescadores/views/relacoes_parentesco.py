from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import RelacaoParentesco
from pescadores.serializers import RelacaoParentescoSerializer

class RelacaoParentescoList(ListCreateAPIView):
    queryset = RelacaoParentesco.objects.all()
    serializer_class = RelacaoParentescoSerializer

class RelacaoParentescoDetail(RetrieveUpdateDestroyAPIView):
    queryset = RelacaoParentesco.objects.all()
    serializer_class = RelacaoParentescoSerializer
