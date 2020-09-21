import django_filters
from .models import Customer, CustomerType

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model=Customer
        fields={
            'id':['iexact'],
            'name':['icontains']
        }

class CustomerTypeFilter(django_filters.FilterSet):
    class Meta:
        model=CustomerType
        fields={
            'id':['iexact'],
            'name':['icontains']
        }