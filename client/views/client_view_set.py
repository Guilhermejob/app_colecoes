from rest_framework import viewsets
from client.models.clients import Client
from client.serializers.client_serializer import ClientSerializer
from rest_framework.views import APIView, Request, Response
from rest_framework import status




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
                return Response({'error':'O colecionador não existe'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Cadastro de cliente
        """
        serializer = ClientSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'massege':'Colecionador cadastrado com sucesso', 'data':serializer.data},
                status=status.HTTP_201_CREATED
            )
            
        return Response(
            {'error':'Erro ao cadastrar o colecionador', 'detais':serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def patch(self, request, id):
        """
        atualiza os dados de um colecionador
        """
        try:
            client = Client.objects.get(pk = id)
        except Client.DoesNotExist:
            return Response({'error': 'O colecionador não existe'}, status=status.HTTP_404_NOT_FOUND)
        
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
            return Response({'error': 'O colecionador não existe'}, status=status.HTTP_404_NOT_FOUND)

        client.delete()
        return Response({"message": "Colecionador removido com sucesso"}, status=status.HTTP_204_NO_CONTENT)
            
    
    

