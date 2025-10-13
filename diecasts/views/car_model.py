from diecasts.models.Car_model import Car_model
from diecasts.serializers.car_model import CarModelSerializer
from rest_framework import viewsets

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car_model.objects.all()
    serializer_class = CarModelSerializer