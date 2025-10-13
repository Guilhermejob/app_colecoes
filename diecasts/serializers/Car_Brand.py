from rest_framework import serializers
from diecasts.models.Car_Brand import Car_Brand


class CarBrandSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Car_Brand
            fields = '__all__'
    
     