from rest_framework import viewsets
from .models import Product, Category, UnitOfMeasurement, ProductCostPrice, ProductSalePrice
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    UnitOfMeasurementSerializer,
    ProductCostPriceSerializer,
    ProductSalePriceSerializer)
from .filters import ProductFilter, CategoryFilter,ProductSellRateFilter


class ProductViewSet(viewsets.ModelViewSet):
    filterset_class = ProductFilter

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    filterset_class=CategoryFilter
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):

    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer


class ProductCostPriceViewSet(viewsets.ModelViewSet):

    queryset = ProductCostPrice.objects.all()
    serializer_class = ProductCostPriceSerializer


class ProductSalePriceViewSet(viewsets.ModelViewSet):
    filterset_class = ProductSellRateFilter

    queryset = ProductSalePrice.objects.all()
    serializer_class = ProductSalePriceSerializer

    