
from diecasts.models import Diecast
from diecasts.serializers.Diecast import DiecastSerializer
from rest_framework import viewsets

class DiecastViewSet(viewsets.ModelViewSet):
    queryset = Diecast.objects.all()
    serializer_class = DiecastSerializer