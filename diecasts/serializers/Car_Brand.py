from rest_framework import serializers
from diecasts.models.Car_Brand import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = CarBrand
            fields = '__all__'
    
     