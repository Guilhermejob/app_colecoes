from diecasts.models import Car_Brand
from diecasts.serializers.Car_Brand import CarBrandSerializer
from rest_framework import viewsets

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = Car_Brand.objects.all()
    serializer_class = CarBrandSerializer