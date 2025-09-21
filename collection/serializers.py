from rest_framework import serializers
from collection.models import Brand, Diecast_Model

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class DiecastModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diecast_Model
        fields = '__all__'
        