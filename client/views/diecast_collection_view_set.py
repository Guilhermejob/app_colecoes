from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from client.models.diecast_collection import DiecastCollection
from client.models.diecast_collection_item import DiecastCollectionItem
from app_collection.models.Diecast import Diecast
from client.serializers.collection_serializer import CollectionSerializer, CollectionItemSerializer

class DiecastCollectionViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollection.objects.all()
    serializer_class = CollectionSerializer
    
    # Post /api/collection/{collection_id}/add_item/
    @action(detail=True, methods=['post'], url_path='add_item')
    def add_item(self, request, pk=None):
        collection = self.get_object()
        diecast_id = request.data.get('diecast_id')
        
        if not diecast_id:
            return Response({"error": "diecast_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            diecast = Diecast.objects.get(id=diecast_id)
        except Diecast.DoesNotExist:
            return Response({"error": "Diecast not found."}, status=status.HTTP_404_NOT_FOUND)
        
        item, created = DiecastCollectionItem.objects.get_or_create(
            collection=collection,
            diecast=diecast,
            defaults={'beginning_date': request.data.get('beginning_date')}
        )
        
        serializer = CollectionItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    
    

class DiecastCollectionsViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollectionItem.objects.all()
    serializer_class = CollectionItemSerializer 
