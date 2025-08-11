from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import PescadorEspecialista
from pescadores.serializers import PescadorEspecialistaSerializer

class PescadorEspecialistaList(ListCreateAPIView):
    queryset = PescadorEspecialista.objects.all()
    serializer_class = PescadorEspecialistaSerializer

class PescadorEspecialistaDetail(RetrieveUpdateDestroyAPIView):
    queryset = PescadorEspecialista.objects.all()
    serializer_class = PescadorEspecialistaSerializer
