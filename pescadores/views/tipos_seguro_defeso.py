from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import TipoSeguroDefeso
from pescadores.serializers import TipoSeguroDefesoSerializer

class TipoSeguroDefesoList(ListCreateAPIView):
    queryset = TipoSeguroDefeso.objects.all()
    serializer_class = TipoSeguroDefesoSerializer

class TipoSeguroDefesoDetail(RetrieveUpdateDestroyAPIView):
    queryset = TipoSeguroDefeso.objects.all()
    serializer_class = TipoSeguroDefesoSerializer
