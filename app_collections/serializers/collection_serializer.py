from rest_framework import serializers
from app_collections.models.diecast_collection import DiecastCollection
from app_collections.models.diecast_collection_item import DiecastCollectionItem
from diecasts.serializers.Diecast import DiecastSerializer
from client.serializers.client_serializer import ClientSerializer
from diecasts.models.Diecast import Diecast

class CollectionItemSerializer(serializers.ModelSerializer):
    collection = serializers.PrimaryKeyRelatedField(queryset=DiecastCollection.objects.all())
    diecasts = serializers.PrimaryKeyRelatedField(queryset=Diecast.objects.all())

    diecast_details = DiecastSerializer(source='diecasts', read_only=True)

    class Meta:
        model = DiecastCollectionItem
        fields = ['id', 'collection', 'diecasts', 'diecast_details', 'created_at']

        
class CollectionSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    items = CollectionItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = DiecastCollection
        fields = '__all__'

    