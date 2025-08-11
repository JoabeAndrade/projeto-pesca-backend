from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import FonteRendaDuranteDefeso
from pescadores.serializers import FonteRendaDuranteDefesoSerializer

class FonteRendaDuranteDefesoList(ListCreateAPIView):
    queryset = FonteRendaDuranteDefeso.objects.all()
    serializer_class = FonteRendaDuranteDefesoSerializer

class FonteRendaDuranteDefesoDetail(RetrieveUpdateDestroyAPIView):
    queryset = FonteRendaDuranteDefeso.objects.all()
    serializer_class = FonteRendaDuranteDefesoSerializer
