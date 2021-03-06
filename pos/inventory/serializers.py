from rest_framework import serializers
from .models import ProductStock, ProductPurchase, Sell, SellItem
class ProductStockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductStock
        fields = '__all__'
        
        
class ProductPurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductPurchase
        fields = '__all__'

class SellItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellItem
        fields = '__all__'
    
class SellSerializer(serializers.ModelSerializer):
    sell = SellItemSerializer(many=False, read_only=True)
    
    class Meta:
        model = Sell
        fields = [
            'sell',
            'id',
            'invoice_no',
            'customer_name',
            'address',
            'gst_no',
            'total_tax',
            'total_discount',
            'total_amount', 
            'date_and_time',
        ]