from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from pescadores.models import Pescador, ArtePesca
from pescadores.serializers import ArtePescaSerializer
from django.shortcuts import get_object_or_404

class ArtePescaList(generics.ListCreateAPIView):
    queryset = ArtePesca.objects.all()
    serializer_class = ArtePescaSerializer

class ArtePescaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtePesca.objects.all()
    serializer_class = ArtePescaSerializer

class ArtesPescaDoPescadorView(APIView):
    def get(self, request, pk_pescador, format=None):
        pesc = get_object_or_404(Pescador, pk=pk_pescador)
        serializer = ArtePescaSerializer(pesc.artes_pesca.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk_pescador, format=None):
        pesc = get_object_or_404(Pescador, pk=pk_pescador)
        arte = get_object_or_404(ArtePesca, pk=request.data.get('id_artepesca'))
        pesc.artes_pesca.add(arte)
        serializer = ArtePescaSerializer(pesc.artes_pesca.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk_pescador, format=None):
        pesc = get_object_or_404(Pescador, pk=pk_pescador)
        arte = get_object_or_404(ArtePesca, pk=request.data.get('id_artepesca'))
        pesc.artes_pesca.remove(arte)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
