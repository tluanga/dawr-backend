from rest_framework import serializers
from .models import CustomerType, Customer

class CustomerTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerType
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

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
        