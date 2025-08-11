from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import EstadoCivil
from pescadores.serializers import EstadoCivilSerializer

class EstadoCivilList(ListCreateAPIView):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer

class EstadoCivilDetail(RetrieveUpdateDestroyAPIView):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer
