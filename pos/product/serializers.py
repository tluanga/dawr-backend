from rest_framework import serializers
from .models import UnitOfMeasurement, Category, Product, ProductCostPrice, ProductSalePrice


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UnitOfMeasurement
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

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


class ProductSalePriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductSalePrice
        fields = '__all__'
