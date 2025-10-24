from app_collections.models.diecast_collection import DiecastCollection
from app_collections.models.diecast_collection_item import DiecastCollectionItem
from app_collections.serializers.collection_serializer import CollectionSerializer, CollectionItemSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from drf_spectacular.utils import extend_schema, extend_schema_view



@extend_schema_view(
    get=extend_schema(responses=CollectionItemSerializer,description="Lista todos os itens de uma coleção ou um item específico."),
    post=extend_schema(request=CollectionItemSerializer,responses={201: CollectionItemSerializer},description="Adiciona um novo item à coleção especificada."),
    patch=extend_schema(request=CollectionItemSerializer,responses={200: CollectionItemSerializer},description="Atualiza parcialmente um item da coleção."),
    delete=extend_schema(responses={204: None},description="Remove um item de uma coleção específica."),
)
class DiecastCollectionItemApiView(APIView):
    """
    Endpoint para gerenciar itens de uma coleçao (GET, POST, PATCH, DELETE)
    """
    

    def get(self, request, collection_id, id=None):
        """
        Retorna todos os itens de uma coleçao ou um item específico dentro dela
        """
        if id:
            try:
                item = DiecastCollectionItem.objects.get(pk=id, collection_id=collection_id)
            except DiecastCollectionItem.DoesNotExist:
                return Response({"error": "Item nao encontrado nessa coleçao"}, status=status.HTTP_404_NOT_FOUND)

            serializer = CollectionItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        items = DiecastCollectionItem.objects.filter(collection_id=collection_id)
        serializer = CollectionItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, collection_id):
        """
        Adiciona um novo item à coleçao especificada
        """
        data = request.data.copy()
        data["collection"] = collection_id  # garante vínculo da coleçao

        serializer = CollectionItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Item adicionado à coleçao com sucesso", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error": "Erro ao adicionar item", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def patch(self, request, collection_id, id):
        """
        Atualiza parcialmente um item de uma coleçao específica
        """
        try:
            item = DiecastCollectionItem.objects.get(pk=id, collection_id=collection_id)
        except DiecastCollectionItem.DoesNotExist:
            return Response({"error": "Item nao encontrado nessa coleçao"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CollectionItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Item atualizado com sucesso", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Erro ao atualizar item", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
        

    def delete(self, request, collection_id, id):
        """
        Remove um item de uma coleçao específica
        """
        try:
            item = DiecastCollectionItem.objects.get(pk=id, collection_id=collection_id)
        except DiecastCollectionItem.DoesNotExist:
            return Response({"error": "Item nao encontrado nessa coleçao"}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response({"message": "Item removido da coleçao com sucesso"}, status=status.HTTP_204_NO_CONTENT)

        

class DiecastCollectionApiView(APIView):
    """
    Endpoint que gerencia as coleções de minaturas do cliente (GET, POST, PATCH, DELETE)
    """

    def get(self, request, id=None):
        """
        Retorna todas as coleções ou uma coleçao especifica pelo ID
        """
        
        if id:
            try:
                collection = DiecastCollection.objects.get(pk=id)
            except DiecastCollection.DoesNotExist:
                return Response({"error": "Coleçao nao encontrada"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = CollectionSerializer(collection)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        
        collections = DiecastCollection.objects.all()
        serializer = CollectionSerializer(collections, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Cria uma nova coleçao
        """
        
        serializer = CollectionSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Message":"Coleçao criada com sucesso", "data":serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error":"Erro ao criar coleçao", "details":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST    
        )
        
    def patch(self, request, id):
        """
        Atualiza os dados da coleçao
        """
        
        try:
            collection = DiecastCollection.objects.get(pk = id)
        except DiecastCollection.DoesNotExist:
            return Response({"Error":"A coleçao nao foi encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CollectionSerializer(collection, data = request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"Coleçao atualizada com sucesso", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"error":"Erro ao atualizar a coleçao", "Details":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, id):
        """
        deleta uma coleçao
        """
        
        try:
            collection = DiecastCollection.objects.get(pk = id)
        except DiecastCollection.DoesNotExist:
            return Response({"error":"A coleçao nao foi encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        collection.delete()
        
        return Response({"message": "Coleçao deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)
