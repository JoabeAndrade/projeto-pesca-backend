from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from pescadores.models import Associacao, Pescador
from pescadores.serializers import AssociacaoSerializer
from django.shortcuts import get_object_or_404

class AssociacaoList(generics.ListCreateAPIView):
    queryset = Associacao.objects.all()
    serializer_class = AssociacaoSerializer

class AssociacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Associacao.objects.all()
    serializer_class = AssociacaoSerializer

class AssociacoesDoPescadorView(APIView):
    def get(self, request, pk_pescador, format=None):
        pescador = get_object_or_404(Pescador, pk=pk_pescador)
        serializer = AssociacaoSerializer(pescador.associacoes.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk_pescador, format=None):
        pescador = get_object_or_404(Pescador, pk=pk_pescador)
        associacao = get_object_or_404(Associacao, pk=request.data.get('associacao_id'))
        pescador.associacoes.add(associacao)
        serializer = AssociacaoSerializer(pescador.associacoes.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk_pescador, format=None):
        pescador = get_object_or_404(Pescador, pk=pk_pescador)
        associacao = get_object_or_404(Associacao, pk=request.data.get('associacao_id'))
        pescador.associacoes.remove(associacao)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
