from rest_framework import serializers
from .models import Product, ProductCostPrice, ProductSellPrice


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    gstcode = serializers.StringRelatedField()
    unit_of_measurement=serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = [
            'id',
            'active',
            'category',
            'name',
            'brand',
            'model',
            'gstcode',
            'cost_price',
            'selling_price',
            'mrp',
            'unit_of_measurement',
            'tag',
            'remarks'
            ]
 


class ProductDetailSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model = Product
        fields='__all__'

class ProductCostPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCostPrice
        fields = '__all__'


class ProductSellPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductSellPrice
        fields = '__all__'
