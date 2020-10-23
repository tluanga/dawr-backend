from rest_framework import viewsets
from .serializers import ProductPurchaseSerializer, ProductStockSerializer
from .models import ProductPurchase, ProductStock
from .filters import ProductStockFilter

class ProductPurchaseViewSet(viewsets.ModelViewSet):
    
    queryset = ProductPurchase.objects.all()
    serializer_class = ProductPurchaseSerializer
    
    
    
class ProductStockViewSet(viewsets.ModelViewSet):
    
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    filterset_class = ProductStockFilter

