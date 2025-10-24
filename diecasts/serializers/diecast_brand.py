from rest_framework import serializers
from diecasts.models.Diecast_Brand import DiecastBrand


class DiecastBrandSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = DiecastBrand
            fields = '__all__'