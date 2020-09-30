from rest_framework import viewsets
from .models import Product,UnitOfMeasurement, ProductCostPrice, ProductSellPrice
from .serializers import (
    ProductSerializer,
    ProductCostPriceSerializer,
    ProductSellPriceSerializer)
from .filters import ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    filterset_class = ProductFilter
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class ProductCostPriceViewSet(viewsets.ModelViewSet):

    queryset = ProductCostPrice.objects.all()
    serializer_class = ProductCostPriceSerializer


class ProductSellPriceViewSet(viewsets.ModelViewSet):
    

    queryset = ProductSellPrice.objects.all()
    serializer_class = ProductSellPriceSerializer

    