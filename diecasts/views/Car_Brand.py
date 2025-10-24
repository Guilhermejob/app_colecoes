from diecasts.models import Car_Brand
from diecasts.serializers.Car_Brand import CarBrandSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(responses=CarBrandSerializer, description="Lista todas as miniaturas."),
    post=extend_schema(request=CarBrandSerializer, responses=CarBrandSerializer, description="Cria uma nova miniatura."),
)
class CarBrandViewSet(APIView):
    
    def get(self, request):
        
        diecasts = Car_Brand.objects.all()
        serializer = CarBrandSerializer(diecasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = CarBrandSerializer(data=request.data)
        
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