from diecasts.models.Car_model import Carmodel
from diecasts.serializers.car_model import CarModelSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(responses=CarModelSerializer, description="Lista todas as miniaturas."),
    post=extend_schema(request=CarModelSerializer, responses=CarModelSerializer, description="Cria uma nova miniatura."),
)
   
class CarModelViewSet(APIView):
    
    def get(self, request):
        
        diecasts = Carmodel.objects.all()
        serializer = CarModelSerializer(diecasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = CarModelSerializer(data=request.data)
        
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