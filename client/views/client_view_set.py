from rest_framework import viewsets
from client.models.clients import Client
from client.serializers.client_serializer import ClientSerializer
from app_collections.serializers.collection_serializer import CollectionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    
    

