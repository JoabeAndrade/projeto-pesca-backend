from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import RelacaoCompanhia
from pescadores.serializers import RelacaoCompanhiaSerializer

class RelacaoCompanhiaList(ListCreateAPIView):
    queryset = RelacaoCompanhia.objects.all()
    serializer_class = RelacaoCompanhiaSerializer

class RelacaoCompanhiaDetail(RetrieveUpdateDestroyAPIView):
    queryset = RelacaoCompanhia.objects.all()
    serializer_class = RelacaoCompanhiaSerializer
