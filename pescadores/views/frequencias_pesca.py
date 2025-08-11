from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import FrequenciaPesca
from pescadores.serializers import FrequenciaPescaSerializer

class FrequenciaPescaList(ListCreateAPIView):
    queryset = FrequenciaPesca.objects.all()
    serializer_class = FrequenciaPescaSerializer

class FrequenciaPescaDetail(RetrieveUpdateDestroyAPIView):
    queryset = FrequenciaPesca.objects.all()
    serializer_class = FrequenciaPescaSerializer
