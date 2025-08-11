from rest_framework import generics
from pescadores.models import InsumoDoPescador
from pescadores.serializers import InsumoDoPescadorSerializer

class InsumoDoPescadorList():
    queryset = InsumoDoPescador.objects.all()
    serializer_class = InsumoDoPescadorSerializer
