from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from pescadores.models import Pescador, AreaPesca
from pescadores.serializers import AreaPescaSerializer
from django.shortcuts import get_object_or_404

class AreaPescaList(generics.ListCreateAPIView):
    queryset = AreaPesca.objects.all()
    serializer_class = AreaPescaSerializer

class AreaPescaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaPesca.objects.all()
    serializer_class = AreaPescaSerializer

class AreasPescaDoPescadorView(APIView):
    def get(self, request, pk_pescador, format=None):
        pescador = get_object_or_404(Pescador, pk=pk_pescador)
        serializer = AreaPescaSerializer(pescador.areas_pesca.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk_pescador, format=None):
        pescador = get_object_or_404(Pescador, pk=pk_pescador)
        area_pesca = get_object_or_404(AreaPesca, pk=request.data.get('id_areapesca'))
        pescador.areas_pesca.add(area_pesca)
        serializer = AreaPescaSerializer(pescador.areas_pesca.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk_pescador, format=None):
        pescador = get_object_or_404(Pescador, pk=pk_pescador)
        area_pesca = get_object_or_404(AreaPesca, pk=request.data.get('id_areapesca'))
        pescador.areas_pesca.remove(area_pesca)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
