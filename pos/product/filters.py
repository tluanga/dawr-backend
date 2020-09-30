
import django_filters
from .models import Product, Category, ProductSellPrice


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'id':['iexact'],
            'name': ['icontains'],
            'model': ['icontains'],
            'tag': ['icontains'],
            'active':['iexact'],
        }

class ProductSellRateFilter(django_filters.FilterSet):
    # product=django_filters.NumberFilter(
    #     lookup_expr='exact'
    # )
    class Meta:
        model = ProductSellPrice
        fields = {
            'product':['exact'],
            'current':['exact']          

        }
