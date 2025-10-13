from rest_framework import viewsets
from app_collections.models.diecast_collection import DiecastCollection
from app_collections.models.diecast_collection_item import DiecastCollectionItem
from app_collections.serializers.collection_serializer import CollectionSerializer, CollectionItemSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollection.objects.all().select_related('owner')
    serializer_class = CollectionSerializer
    
class CollectionItemViewSet(viewsets.ModelViewSet):
    queryset = DiecastCollectionItem.objects.all().select_related("collection", "diecasts")
    serializer_class = CollectionItemSerializer

