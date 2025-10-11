from app_collection.models import Car_Brand
from app_collection.serializers.Car_Brand import CarBrandSerializer
from rest_framework import viewsets

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = Car_Brand.objects.all()
    serializer_class = CarBrandSerializer