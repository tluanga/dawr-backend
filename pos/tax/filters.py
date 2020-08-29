import django_filters
from .models import GSTCode

class GSTCodeFilter(django_filters.FilterSet):
    class Meta:
        model=GSTCode
        fields={
            'id':['iexact'],
            'code':['icontains'],
            'description':['icontains'],
            'remarks':['icontains']

        }