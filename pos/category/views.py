from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from .filters import CategoryFilter

class CategoryViewSet(viewsets.ModelViewSet):
    filterset_class=CategoryFilter
    queryset = Category.objects.all()
    serializer_class = CategorySerializer