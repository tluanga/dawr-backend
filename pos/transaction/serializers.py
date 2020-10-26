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
        # fields='__all__'
        fields = [
            'ref_no',
            'total_tax',
            'total_discount',
            'total_amount',
            'date',
            'remarks',
            'warehouse',
            'supplier',
            'purchase_order_item'
        ]
    def create(self, validated_data):
        purchase_order_items_data = validated_data.pop('purchase_order_item')
        print('purchase_order_items_data',purchase_order_items_data)
        _purchase = PurchaseOrder.objects.create(**validated_data)
        print('purchase variable/n',str(_purchase))
        for purchase_order_item_data in purchase_order_items_data:
            PurchaseOrderItem.objects.create(
                purchase_order=_purchase,
                **purchase_order_item_data
                )
        return purchase_order


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