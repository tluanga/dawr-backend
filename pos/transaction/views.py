from rest_framework import viewsets
from .serializers import (ProductStockSerializer, 
        PurchaseOrderSerializer, PurchaseOrderItemSerializer)
from .models import (ProductStock, PurchaseOrder,PurchaseOrderItem )
from .filters import ProductStockFilter

class ProductStockViewSet(viewsets.ModelViewSet):
    
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    filterset_class = ProductStockFilter


class PurchaseOrderViewSet(viewsets.ModelViewSet):

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

  
    

