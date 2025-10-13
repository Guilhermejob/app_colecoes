from diecasts.models import Diecast_Model
from diecasts.serializers.Diecast_Model import DiecastModelSerializer
from rest_framework import viewsets

class DiecastModelViewSet(viewsets.ModelViewSet):
    queryset = Diecast_Model.objects.all()
    serializer_class = DiecastModelSerializer