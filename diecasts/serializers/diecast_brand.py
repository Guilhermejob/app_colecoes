from rest_framework import serializers
from diecasts.models.Diecast_Brand import Diecast_Brand


class DiecastBrandSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Diecast_Brand
            fields = '__all__'