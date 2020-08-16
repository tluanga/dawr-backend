from rest_framework import serializers
from .models import WareHouse

class WareHouseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WareHouse
        fields = '__all__'