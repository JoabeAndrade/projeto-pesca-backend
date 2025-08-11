from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pescadores.models import EmissorRgp
from pescadores.serializers import EmissorRgpSerializer

class EmissorRgpList(ListCreateAPIView):
    queryset = EmissorRgp.objects.all()
    serializer_class = EmissorRgpSerializer

class EmissorRgpDetail(RetrieveUpdateDestroyAPIView):
    queryset = EmissorRgp.objects.all()
    serializer_class = EmissorRgpSerializer
