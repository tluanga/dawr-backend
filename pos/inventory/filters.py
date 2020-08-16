from django_filters import rest_framework as filters
from .models import ProductStock

class ProductStockFilter(filters.FilterSet):
    product = filters.NumberFilter(lookup_expr='exact')
    current=filters.BooleanFilter()
    
    class Meta:
        model = ProductStock
        fields={'product','current'}
