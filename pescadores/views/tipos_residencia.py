from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import TipoResidencia
from pescadores.serializers import TipoResidenciaSerializer

class TipoResidenciaList(ListCreateAPIView):
    queryset = TipoResidencia.objects.all()
    serializer_class = TipoResidenciaSerializer

class TipoResidenciaDetail(RetrieveUpdateDestroyAPIView):
    queryset = TipoResidencia.objects.all()
    serializer_class = TipoResidenciaSerializer
