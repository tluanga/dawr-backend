from rest_framework import serializers
from .models import OrderItem, Order

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'product',
            'quantity',
            'sell_rate'
            ]




class OrderSerializer(serializers.ModelSerializer):
    orderItem=OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'ref_code',
            'orderItem',
            'cash_received',
            'discount',
            'cash_rounded_off',
            'remarks'
        ]
    
    def create(self, validated_data):
        orderitems_data = validated_data.pop('orderItem')
        order = Order.objects.create(**validated_data)
        for orderitem_data in orderitems_data:
            OrderItem.objects.create(
                order=order,
                **orderitem_data
                )
        return order
