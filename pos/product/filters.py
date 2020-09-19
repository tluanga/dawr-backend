
import django_filters
from .models import Product, Category


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'id':['iexact'],
            'name': ['icontains'],
            'model': ['icontains'],
            'tag': ['icontains']
        }
class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'id':['iexact'],
            'name': ['icontains'],
            'abbreviation':['icontains'],

        }

# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = Product
#         fields = ['price', 'release_date']
