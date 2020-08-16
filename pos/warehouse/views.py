from rest_framework import viewsets
from .models import WareHouse
from .serializers import WareHouseSerializer

class WareHouseViewSet(viewsets.ModelViewSet):
    
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer