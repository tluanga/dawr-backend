from django.db import models
# from pos.inventory.models import ProductStock


class ProductQuerySet(models.QuerySet):
    def getActiveProduct(self):
        return self.filter(Active=True)
    def getProductDetail(self):
        return self.filter(active=True).filter(
            productstock__quantity__gt=0
        )


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)
    
    def getProductDetail(self):
        return self.get_queryset().getProductDetail()


