from rest_framework import serializers
from app_collection.models.Diecast_Model import Diecast_Model


class DiecastModelSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Diecast_Model
            fields = '__all__'