
from diecasts.models import Diecast
from diecasts.serializers.Diecast import DiecastSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#---- Versão automatica usando do ModelViewSet para a prototipação rápida

"""
from rest_framework import viewsets

class DiecastViewSet(viewsets.ModelViewSet):
    queryset = Diecast.objects.all()
    serializer_class = DiecastSerializer
"""

class DiecastApiView(APIView):
    
    """
    Endpoint para cadastro de uma miniatura diecast
    """
    
    def get(self, request):
        
        diecasts = Diecast.objects.all()
        serializer = DiecastSerializer(diecasts, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DiecastSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({
                "message":"Miniatura cadastrada com sucesso",
                "data":serializer.data}, 
                status=status.HTTP_201_CREATED)
            
        return Response({
            "error":"Erro ao cadastrar a miniatura",
            "details":serializer.errors    
        }
        , status=status.HTTP_400_BAD_REQUEST)
        
class DiecastDetailApiView(APIView):
    
    def get(self, request, pk):
        
        try:
            diecast = Diecast.objects.get(pk=pk)
        except Diecast.DoesNotExist:
            return Response(
                {"error":"Miniatura não encontrada",},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = DiecastSerializer(diecast)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
