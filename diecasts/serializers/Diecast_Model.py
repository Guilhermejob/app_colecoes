from rest_framework import serializers
from diecasts.models.Diecast_Model import DiecastModel


class DiecastModelSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = DiecastModel
            fields = '__all__'