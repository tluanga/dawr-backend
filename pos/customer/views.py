from rest_framework import viewsets
from .models import CustomerType, Customer
from .serializers import CustomerTypeSerializer, CustomerSerializer
from .filters import CustomerFilter, CustomerTypeFilter

class CustomerTypeViewSet(viewsets.ModelViewSet):
    filterset_class = CustomerTypeFilter
    queryset = CustomerType.objects.all()
    serializer_class = CustomerTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    filterset_class = CustomerFilter
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

