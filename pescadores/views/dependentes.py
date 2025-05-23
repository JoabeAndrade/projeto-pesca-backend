from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pescadores.models import Dependente
from pescadores.serializers import DependenteSerializer

class DependenteView(APIView):
    def post(self, request):
        serializer = DependenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = get_object_or_404(Dependente, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
