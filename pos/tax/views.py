from rest_framework import viewsets
from .models import GSTCode
from .serializers import GSTCodeSerializer
from .filters import GSTCodeFilter

class GSTCodeViewSet(viewsets.ModelViewSet):
    filterset_class=GSTCodeFilter
    
    queryset = GSTCode.objects.all()
    serializer_class = GSTCodeSerializer