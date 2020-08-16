from rest_framework import viewsets
from .models import CustomerType, Customer
from .serializers import CustomerTypeSerializer, CustomerSerializer

class CustomerTypeViewSet(viewsets.ModelViewSet):

    queryset = CustomerType.objects.all()
    serializer_class = CustomerTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

