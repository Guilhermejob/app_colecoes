from collection.models import Brand, Diecast_Model
from collection.serializers import BrandSerializer, DiecastModelSerializer
from rest_framework import viewsets

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class DiecastModelViewSet(viewsets.ModelViewSet):
    queryset = Diecast_Model.objects.all()
    serializer_class = DiecastModelSerializer
    
