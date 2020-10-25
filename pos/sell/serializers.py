from rest_framework import serializers
from .models import OrderItem, Order, ModeOfSell,SettleBill

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'product',
            'quantity',
            'sell_price',
            'discount',
            'tax_code',
            'tax_price',
            'amount'
            ]




class OrderSerializer(serializers.ModelSerializer):
    orderItem=OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_date',
            'ref_code',
            'orderItem',
            'cash_received',
            'total_discount',
            'total_tax',
            'total_amount',
            'mode',
            'remarks',
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

        

class ModeOfSellSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModeOfSell
        fields = '__all__'



class SettleBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SettleBill
        fields = '__all__'