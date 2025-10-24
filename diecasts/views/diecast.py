
from diecasts.models import Diecast
from diecasts.serializers.Diecast import DiecastSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..filters.diecast_filter import DiecastFilter
from drf_spectacular.utils import extend_schema, extend_schema_view

"""
----- Versao automatica usando do ModelViewSet para a prototipaçao rápida

from rest_framework import viewsets

class DiecastViewSet(viewsets.ModelViewSet):
    queryset = Diecast.objects.all()
    serializer_class = DiecastSerializer
"""

@extend_schema_view(
    get=extend_schema(responses=DiecastSerializer, description="Lista todas as miniaturas."),
    post=extend_schema(request=DiecastSerializer, responses=DiecastSerializer, description="Cria uma nova miniatura."),
    patch=extend_schema(request=DiecastSerializer, responses=DiecastSerializer, description="Atualiza parcialmente."),
    delete=extend_schema(responses={204: None}, description="Deleta uma miniatura."),
)

class DiecastApiView(APIView):
    
    """
    Endpoint para listagem e cadastro de miniaturas Diecast.
    """
    def get(self, request):
        if not request.query_params:
            diecasts = Diecast.objects.all()
            serializer = DiecastSerializer(diecasts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        diecast_filter = DiecastFilter(request.query_params, queryset=Diecast.objects.all())
        
        if not diecast_filter.qs.exists():
            return Response(
                {'message':'Nenhum resultado encontrado para os filtros desejados'}
            )
            
        serializer = DiecastSerializer(diecast_filter.qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
      
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
    
    def get(self, request, id):
        
        try:
            diecast = Diecast.objects.get(pk=id)
        except Diecast.DoesNotExist:
            return Response(
                {"error":"Miniatura nao encontrada",},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = DiecastSerializer(diecast)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        
        print(f"---------------- {id} ---------------------")
        try:
            diecast = Diecast.objects.get(pk = id)
        except Diecast.DoesNotExist:
            return Response(
                {"error":"A miniatura nao existe",},
                status = status.HTTP_404_NOT_FOUND
            )
            
        serializer = DiecastSerializer(diecast, data = request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
