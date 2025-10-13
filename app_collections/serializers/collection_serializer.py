from rest_framework import serializers
from app_collections.models.diecast_collection import DiecastCollection
from app_collections.models.diecast_collection_item import DiecastCollectionItem
from diecasts.serializers.Diecast import DiecastSerializer
from client.serializers.client_serializer import ClientSerializer

class CollectionItemSerializer(serializers.ModelSerializer):
    # Retorna apenas o nome da coleção
    collection = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    # Retorna os detalhes completos da miniatura (usando o DiecastSerializer)
    diecasts = DiecastSerializer(read_only=True)

    class Meta:
        model = DiecastCollectionItem
        fields = '__all__'
        
class CollectionSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    items = CollectionItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = DiecastCollection
        fields = '__all__'

    