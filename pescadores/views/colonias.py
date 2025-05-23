from rest_framework import generics
from pescadores.models import Colonia
from pescadores.serializers import ColoniaSerializer

class ColoniaList(generics.ListCreateAPIView):
    queryset = Colonia.objects.all()
    serializer_class = ColoniaSerializer

class ColoniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colonia.objects.all()
    serializer_class = ColoniaSerializer
