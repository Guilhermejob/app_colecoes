from app_collection.models.Car_model import Car_model
from app_collection.serializers.car_model import CarModelSerializer
from rest_framework import viewsets

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car_model.objects.all()
    serializer_class = CarModelSerializer