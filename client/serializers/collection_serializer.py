from rest_framework import serializers
from client.models.diecast_collection import DiecastCollection
from client.models.diecast_collection_item import DiecastCollectionItem
from app_collection.serializers.Diecast import DiecastSerializer
from client.serializers.client_serializer import ClientSerializer

class CollectionItemSerializer(serializers.ModelSerializer):
    
    diecast = DiecastSerializer(read_only=True)

    
    class Meta:
        model = DiecastCollectionItem
        fields = '__all__'
        
class CollectionSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    items = CollectionItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = DiecastCollection
        fields = '__all__'

    