from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from .manager import ProductManager


from pos.tax.models import GSTCode


class UnitOfMeasurement(models.Model):
    
    unit_of_measurement = models.CharField(max_length=255)
    abbreviation=models.CharField(max_length=100)
    type_of_measurement = models.CharField(max_length=255)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.unit_of_measurement


class Category(models.Model):
    name = models.CharField(max_length=250)
    abbreviation=models.CharField(max_length=10)    
    description=models.CharField(max_length=500,blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product')
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    tag = models.CharField(max_length=250, null=True)
    remarks = models.TextField(null=True)
    hsn_code = models.ForeignKey(
        GSTCode, on_delete=models.CASCADE, related_name='product', null=True)
    unit_of_measurement = models.ForeignKey(
        UnitOfMeasurement, on_delete=models.DO_NOTHING, related_name='category')
    active = models.BooleanField(default=True)
    # picture
    objects=ProductManager()
    # select the product where active=true & quantity<0
    def __str__(self):
        return self.name
# Call the real save() method


class ProductCostPrice(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='productcostprice')
    per_piece_cost_price = models.IntegerField(blank=True, null=True)
    per_bulk_cost_price = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=True)
    active=models.BooleanField(default=True)

    @staticmethod
    def CreateCostPrice(product, bulk, per_piece_cost_price=0, per_bulk_cost_price=0):

        try:
            currentprice = ProductCostPrice.objects.filter(
                product=product.id).latest('time')
            currentprice.current = False
            currentprice.save()
            productCostPrice = ProductCostPrice.objects.create(
                product=product,
                per_piece_cost_price=per_piece_cost_price,
                per_bulk_cost_price=per_bulk_cost_price,
                current=True
            )
            return productCostPrice
        except ProductCostPrice.DoesNotExist:
            productCostPrice = ProductCostPrice.objects.create(
                product=product,
                per_piece_cost_price=per_piece_cost_price,
                per_bulk_cost_price=per_bulk_cost_price,
                current=True
            )
            return productCostPrice

    @staticmethod
    def GetCurrentPerPieceCostPrice(product):
        current_per_piece_cost_price = ProductCostPrice.objects.filter(
            product=product.id).latest('time').per_piece_cost_price
        return current_per_piece_cost_price

    @staticmethod
    def GetCurrentPerBulkCostPric(product):
        current_per_bulk_cost_price = ProductCostPrice.objects.filter(
            product=product.id).latest('time').per_bulk_cost_price
        return current_per_bulk_cost_price

    def __str__(self):
        return str(product)


class ProductSellPrice(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='productsaleprice')
    per_piece_sell_price = models.IntegerField(blank=True, null=True)
    per_bulk_sell_price = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=True)
    active=models.BooleanField(default=True)

    @staticmethod
    def GetCurrentPerPieceSellPrice(product):
        current_per_piece_sell_Price = ProductSellPrice.objects.filter(
            product=product.id).latest('time').per_piece_sell_price
        return current_per_piece_sell_Price

    @staticmethod
    def GetCurrentPerBulkSellPrice(product):
        current_per_bulk_sell_price = ProductSellPrice.objects.filter(
            product=product.id).latest('time').per_bulk_sell_price
        return current_per_bulk_sell_price

    @staticmethod
    def CreateSellPrice(product, bulk, per_piece_sell_price=0, per_bulk_sell_price=0):

        try:
            currentprice = ProductSellPrice.objects.filter(
                product=product.id).latest('time')
            currentprice.current = False
            currentprice.save()
            productSellPrice = ProductSellPrice.objects.create(
                product=product,
                per_piece_sell_price=per_piece_sell_price,
                per_bulk_sell_price=per_bulk_sell_price,
                current=True
            )
            return productSellPrice
        except ProductSellPrice.DoesNotExist:
            productSellPrice = ProductSellPrice.objects.create(
                product=product,
                per_piece_sell_price=per_piece_sell_price,
                per_bulk_sell_price=per_bulk_sell_price,
                current=True
            )
            return productSellPrice

    def __str__(self):
        return str(product)

class MaximumRetailPrice(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='mrp')
    mrp = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=True)
    active=models.BooleanField(default=True)

    @staticmethod
    def CreateMrp(product, bulk, mrp=0):
        try:
            currentprice = MaximumRetailPrice.objects.filter(
                product=product.id).latest('time')
            currentprice.current = False
            currentprice.save()
            mrp = MaximumRetailPrice.objects.create(
                product=product,
                mrp=mrp,
                current=True
            )
            return mrp
        except MaximumRetailPrice.DoesNotExist:
            mrp = MaximumRetailPrice.objects.create(
                product=product,
                mrp=mrp,
                current=True
            )
            return mrp


# class ProductPrice(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_price')
#     per_piece_cost_price=models.IntegerField(blank=True, null=True)
#     per_bulk_cost_price=models.IntegerField(blank=True, null=True)
#     per_piece_sell_price=models.IntegerField(blank=True, null=True)
#     per_bulk_sell_price=models.IntegerField(blank=True, null=True)
#     time=models.DateTimeField(auto_now_add=True)
#     current=models.BooleanField(default=True)

#     @staticmethod
#     def CreateCostPrice(product,bulk,per_piece_cost_price=0,per_bulk_cost_price=0):
#         #currentprice=productPrice.objects.filter(product=product.id).latest('time')
#         #currentprice.current=False
#         #currentprice.save()
#         ProductPrice.objects.create(
#             product=product,
#             per_piece_cost_price=per_piece_cost_price,
#             per_bulk_cost_price=per_bulk_cost_price
#         )
#     @staticmethod
#     def CreateSellPrice(product,per_piece_sell_price,per_bulk_price):
#         ProductPrice.objects.create(
#             product=product,
#             per_piece_sell_price=per_piece_sell_price,
#             per_bulk_price=per_bulk_price
#         )

#     @staticmethod
#     def GetCurrentPerPieceCostPrice(product):
#         current_per_piece_cost_price=ProductPrice.objects.filter(product=product.id).latest('time').per_piece_cost_price
#         return current_per_piece_cost_price

#     @staticmethod
#     def GetCurrentPerBulkCostPrice(product):
#         current_per_bulk_cost_price=ProductPrice.objects.filter(product=product.id).latest('time').per_bulk_cost_price
#         return current_per_bulk_cost_price

#     @staticmethod
#     def GetCurrentPerPieceSellPrice(product):
#         current_per_piece_sell_price=ProductPrice.objects.filter(product=product.id).latest('time').per_piece_sell_price
#         return current_per_piece_sell_price

#     @staticmethod
#     def GetCurrentPerBulkSellPrice(product):
#         current_per_bulk_sell_price=ProductPrice.objects.filter(product=product.id).latest('time').per_bulk_sell_price
#         return current_per_bulk_sell_price
