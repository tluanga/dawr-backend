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
    purchase_order_items=PurchaseOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = PurchaseOrder
        fields = [
            'id',
            'ref_no',
            'total_tax',
            'total_discount',
            'total_amount',
            'date',
            'remarks',
            'warehouse',
            'supplier',
            'purchase_order_items'
        ]
    # def create(self, validated_data):
    #     purchase_order_items_data = validated_data.pop('purchase_order_items')
    #     purchase_order= PurchaseOrder.objects.create(**validated_data)
    #     print('purchase_order_items_data',purchase_order_items_data)
    #     print('purchase_order',purchase_order)
    #     return purchase_order
        # for purchase_order_item_data in purchase_order_items_data:
        #     PurchaseOrderItem.objects.create(purchase_order=purchase_order, **purchase_order_item_data)
        # return purchase_order


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