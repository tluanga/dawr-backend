from django.urls import path
from .views import ProductWithFilters
urlpatterns = [
    path('filters', ProductWithFilters)
]