from rest_framework import serializers
from .models import (ProductStock,PurchaseOrder,PurchaseOrderItem)
# Sell, SellItem
class ProductStockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductStock
        fields = '__all__'
        
class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_order_item=PurchaseOrderItemSerializer(many=True)
    class Meta:
        model = PurchaseOrder
        fields = [
            'ref_no',
            'total_tax',
            'discount',
            'total_amount',
            'time',
            'remarks',
            'warehouse',
            'supplier',
            'purchase_order_item'
        ]



'''
class SellItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellItem
        fields = '__all__'
    
class SellSerializer(serializers.ModelSerializer):
    sell = SellItemSerializer(many=true, read_only=True)
    
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
    '''