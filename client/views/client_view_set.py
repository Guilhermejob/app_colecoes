from rest_framework import viewsets
from client.models.clients import Client
from client.serializers.client_serializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
