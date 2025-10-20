from diecasts.models.Diecast_Brand import Diecast_Brand
from diecasts.serializers.diecast_brand import DiecastBrandSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DiecastBrandViewSet(APIView):
    
    def get(self, request):
        
        diecasts = Diecast_Brand.objects.all()
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