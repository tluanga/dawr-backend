from rest_framework import viewsets
from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer
from .filters import OrderFilter


class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class=OrderFilter