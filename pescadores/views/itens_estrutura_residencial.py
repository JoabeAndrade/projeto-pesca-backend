from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import ItemEstruturaResidencial
from pescadores.serializers import ItemEstruturaResidencialSerializer

class ItemEstruturaResidencialList(ListCreateAPIView):
    queryset = ItemEstruturaResidencial.objects.all()
    serializer_class = ItemEstruturaResidencialSerializer

class ItemEstruturaResidencialDetail(RetrieveUpdateDestroyAPIView):
    queryset = ItemEstruturaResidencial.objects.all()
    serializer_class = ItemEstruturaResidencialSerializer
