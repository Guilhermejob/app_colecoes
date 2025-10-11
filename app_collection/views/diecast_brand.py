from app_collection.models.Diecast_Brand import Diecast_Brand
from app_collection.serializers.diecast_brand import DiecastBrandSerializer
from rest_framework import viewsets

class DiecastBrandViewSet(viewsets.ModelViewSet):
    queryset = Diecast_Brand.objects.all()
    serializer_class = DiecastBrandSerializer