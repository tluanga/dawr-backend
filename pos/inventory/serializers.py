from rest_framework import serializers
from .models import ProductStock,  ProductPurchase

class ProductStockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductStock
        fields = '__all__'
        
        
class ProductPurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductPurchase
        fields = '__all__'
