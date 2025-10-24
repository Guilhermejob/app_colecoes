from diecasts.models import DiecastModel
from diecasts.serializers.Diecast_Model import DiecastModelSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(responses=DiecastModelSerializer, description="Lista todas as miniaturas."),
    post=extend_schema(request=DiecastModelSerializer, responses=DiecastModelSerializer, description="Cria uma nova miniatura."),
)

class DiecastModelViewSet(APIView):
    
    def get(self, request):
        
        diecasts = DiecastModel.objects.all()
        serializer = DiecastModelSerializer(diecasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = DiecastModelSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response({
                'message':'modelo de miniatura cadastrado com sucesso',
                'data':serializer.data},
                status=status.HTTP_201_CREATED)
        
        return Response({
            "error":"Erro ao cadastrar o modelo miniatura",
            "details":serializer.errors    
        }
        , status=status.HTTP_400_BAD_REQUEST)
        
        
        
    