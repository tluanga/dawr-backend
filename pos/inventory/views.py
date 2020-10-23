from rest_framework import viewsets
from .serializers import ProductPurchaseSerializer, ProductStockSerializer, SellItemSerializer, SellSerializer
from .models import ProductPurchase, ProductStock, SellItem, Sell
from .filters import ProductStockFilter

class ProductPurchaseViewSet(viewsets.ModelViewSet):
    
    queryset = ProductPurchase.objects.all()
    serializer_class = ProductPurchaseSerializer
    
    
    
class ProductStockViewSet(viewsets.ModelViewSet):
    
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    filterset_class = ProductStockFilter

class SellItemViewSet(viewsets.ModelViewSet):
    
    queryset = SellItem.objects.all()
    serializer_class = SellItemSerializer

class SellViewSet(viewsets.ModelViewSet):
    
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

