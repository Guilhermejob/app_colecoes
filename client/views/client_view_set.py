from rest_framework import viewsets
from client.models.clients import Client
from client.serializers.client_serializer import ClientSerializer
from rest_framework.views import APIView, Request, Response




class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class GetClientById(APIView):
    
    def get(self, request:Request, id:int) -> Response:
        
        try:
            client = Client.objects.get(pk = id)
        except Client.DoesNotExist:
            return Response({'error':'O colecionador não exitste'}, 404)
        
        serializer = ClientSerializer(client)
        
        return Response(serializer.data, status=200)
    
    
    

