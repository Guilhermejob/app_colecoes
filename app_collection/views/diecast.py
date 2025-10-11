
from app_collection.models import Diecast
from app_collection.serializers.Diecast import DiecastSerializer
from rest_framework import viewsets

class DiecastViewSet(viewsets.ModelViewSet):
    queryset = Diecast.objects.all()
    serializer_class = DiecastSerializer