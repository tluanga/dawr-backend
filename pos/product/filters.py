
import django_filters
from .models import Product, Category, ProductSellPrice


import django_filters



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
class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'id':['iexact'],
            'name': ['icontains'],
            'abbreviation':['icontains'],

        }
class ProductSellPriceFilter(django_filters.FilterSet):
    # product=django_filters.NumberFilter(
    #     lookup_expr='exact'
    # )
    class Meta:
        model = ProductSellPrice
        fields = {
            'product':['exact'],
            'current':['exact']          

        }
