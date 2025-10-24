from diecasts.models.Diecast_Brand import DiecastBrand
from diecasts.serializers.diecast_brand import DiecastBrandSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(responses=DiecastBrandSerializer, description="Lista todas as miniaturas."),
    post=extend_schema(request=DiecastBrandSerializer, responses=DiecastBrandSerializer, description="Cria uma nova miniatura."),
)

class DiecastBrandViewSet(APIView):
    
    def get(self, request):
        
        diecasts = DiecastBrand.objects.all()
        serializer = DiecastBrandSerializer(diecasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = DiecastBrandSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response({
                'message':'Marca da miniatura cadastrada com sucesso',
                'data':serializer.data},
                status=status.HTTP_201_CREATED)
        
        return Response({
            "error":"Erro ao cadastrar a marca miniatura",
            "details":serializer.errors    
        }
        , status=status.HTTP_400_BAD_REQUEST)