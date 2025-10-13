from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from client.models.diecast_collection import DiecastCollection
from client.models.diecast_collection_item import DiecastCollectionItem
from app_collection.models.Diecast import Diecast
from client.serializers.collection_serializer import CollectionSerializer, CollectionItemSerializer

'''class DiecastCollectionViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollection.objects.all()
    serializer_class = CollectionSerializer

    @action(detail=True, methods=["post"], url_path="add_item/(?P<diecast_id>[^/.]+)")
    def add_item(self, request, pk=None, diecast_id=None):
        """
        Adiciona uma miniatura (Diecast) à coleção especificada.
        Ex: POST /api/collections/{id_collection}/add_item/{id_diecast}/
        """
        try:
            collection = self.get_object()
            diecast = Diecast.objects.get(id=diecast_id)
            collection.items.add(diecast)
            return Response({
                "message": f"Miniatura '{diecast}' adicionada à coleção '{collection.name}' com sucesso."
            }, status=status.HTTP_200_OK)
        except Diecast.DoesNotExist:
            return Response({"error": "Diecast não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    

class DiecastCollectionsViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollectionItem.objects.all()
    serializer_class = CollectionItemSerializer 
    
'''

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollection.objects.all().select_related('owner')
    serializer_class = CollectionSerializer
    
class CollectionItemViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollectionItem.objects.all().select_related("collection", "diecasts")
    serializer_class = CollectionItemSerializer

