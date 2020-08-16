from rest_framework import viewsets
from .models import GSTCode
from .serializers import GSTCodeSerializer

class GSTCodeViewSet(viewsets.ModelViewSet):
    
    queryset = GSTCode.objects.all()
    serializer_class = GSTCodeSerializer