from rest_framework import generics
from pescadores.models import Municipio
from pescadores.serializers import MunicipioSerializer

class MunicipioList(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class MunicipioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
