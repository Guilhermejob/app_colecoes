from rest_framework import viewsets
from client.models.clients import Client
from client.serializers.client_serializer import ClientSerializer
from rest_framework.views import APIView, Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view



@extend_schema_view(
    get=extend_schema(responses=ClientSerializer, description="Lista todas as miniaturas."),
    post=extend_schema(request=ClientSerializer, responses=ClientSerializer, description="Cria uma nova miniatura."),
    patch=extend_schema(request=ClientSerializer, responses=ClientSerializer, description="Atualiza parcialmente."),
    delete=extend_schema(responses={204: None}, description="Deleta uma miniatura."),
)
class ClientApiView(APIView):
    """
    Endpoint responsavel pelo Crud de colecionadores(Client)
    """
    def get(self, request, id=None):
        """
        Retorna todos os colecionadores ou um especifico por ID
        """
        
        if id:
            try:
                client = Client.objects.get(pk = id)
            except Client.DoesNotExist:
                return Response({'error':'O colecionador nao existe'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        """
        atualiza os dados de um colecionador
        """
        try:
            client = Client.objects.get(pk = id)
        except Client.DoesNotExist:
            return Response({'error': 'O colecionador nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientSerializer(client, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Colecionador atualizado com sucesso", "data": serializer.data},
                status=status.HTTP_200_OK)
            
        return Response(
            {"error": "Erro ao atualizar o colecionador", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
    def delete(self, request, id):
        """
        Exclui um colecionador pelo ID
        """
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response({'error': 'O colecionador nao existe'}, status=status.HTTP_404_NOT_FOUND)

        client.delete()
        return Response({"message": "Colecionador removido com sucesso"}, status=status.HTTP_204_NO_CONTENT)
            
    
    

