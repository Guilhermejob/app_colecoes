from rest_framework import serializers
from app_collection.models.Car_model import Car_model


class CarModelSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Car_model
            fields = '__all__'