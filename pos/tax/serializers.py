from rest_framework import serializers
from .models import GSTCode

class GSTCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GSTCode
        fields = '__all__'