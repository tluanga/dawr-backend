from rest_framework import viewsets
from .models import Product, Category, UnitOfMeasurement, ProductCostPrice, ProductSellPrice, MaximumRetailPrice
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    UnitOfMeasurementSerializer,
    ProductCostPriceSerializer,
    ProductSellPriceSerializer,
    MaximumRetailPriceSerializer)
from .filters import ProductFilter, CategoryFilter,ProductSellPriceFilter


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


class ProductSellPriceViewSet(viewsets.ModelViewSet):
    filterset_class = ProductSellPriceFilter

    queryset = ProductSellPrice.objects.all()
    serializer_class = ProductSellPriceSerializer

from rest_framework import generics
from django_filters import rest_framework as filters


class ProductWithFilters(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('brand', 'model')

class MaximumRetailPriceViewSet(viewsets.ModelViewSet):

    queryset = MaximumRetailPrice.objects.all()
    serializer_class = ProductCostPriceSerializer