from rest_framework import serializers
from diecasts.models.Car_model import Carmodel


class CarModelSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Carmodel
            fields = '__all__'