from rest_framework import viewsets
from .serializers import PurchaseOrderItemSerializer, ProductStockSerializer
from .models import PurchaseOrderItem, ProductStock
from .filters import ProductStockFilter

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    
    
    
class ProductStockViewSet(viewsets.ModelViewSet):
    
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    filterset_class = ProductStockFilter

