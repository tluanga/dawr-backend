from rest_framework import serializers
from .models import CustomerType, Customer

class CustomerTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerType
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    customer_type=serializers.StringRelatedField()

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'address',
            'city',
            'contact_no',
            'email',
            'gst_no',
            'customer_type',
        ]
        