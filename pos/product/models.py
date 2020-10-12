from django.db import models
from pos.category.models import Category
from pos.unit_of_measurement.models import UnitOfMeasurement
from django.core.exceptions import ValidationError
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from .manager import ProductManager


from pos.tax.models import GSTCode




class Product(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product')
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    tag = models.CharField(max_length=250, null=True, blank=True)
    remarks = models.TextField(null=True)
    gstcode = models.ForeignKey(
        GSTCode, on_delete=models.CASCADE, related_name='product', null=True)
    cost_price=models.DecimalField(decimal_places=2,blank=True, null=True, max_digits=6)
    selling_price = models.DecimalField(
        decimal_places=2, blank=True, null=True, max_digits=6)
    mrp = models.IntegerField(blank=True, null=True)
    unit_of_measurement = models.ForeignKey(
        UnitOfMeasurement, on_delete=models.DO_NOTHING, related_name='category')
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

    @staticmethod
    def CreateBuyRate(product, bulk, per_piece_cost_price=0, per_bulk_cost_price=0):

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
        current_per_piece_buy_rate = ProductCostPrice.objects.filter(
            product=product.id).latest('time').per_piece_buy_rate
        return current_per_piece_buy_rate

    @staticmethod
    def GetCurrentPerBulkCostPric(product):
        current_per_bulk_buy_rate = ProductCostPrice.objects.filter(
            product=product.id).latest('time').per_bulk_buy_rate
        return current_per_bulk_buy_rate

    def __str__(self):
        return str(product)


class ProductSellPrice(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='productsellrate')
    per_piece_sell_price = models.IntegerField(blank=True, null=True)
    per_bulk_sell_price = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=True)

    @staticmethod
    def GetCurrentPerPieceSellRate(product):
        current_per_piece_sell_Price = ProductSellPrice.objects.filter(
            product=product.id).latest('time').per_piece_sell_rate
        return current_per_piece_sell_Price

    @staticmethod
    def GetCurrentPerBulkSellRate(product):
        current_per_bulk_sell_price = ProductSellPrice.objects.filter(
            product=product.id).latest('time').per_bulk_sell_rate
        return current_per_bulk_sell_price

    @staticmethod
    def CreateSellRate(product, bulk, per_piece_sell_price=0, per_bulk_sell_price=0):

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



# class ProductRate(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_rate')
#     per_piece_buy_rate=models.IntegerField(blank=True, null=True)
#     per_bulk_buy_rate=models.IntegerField(blank=True, null=True)
#     per_piece_sell_rate=models.IntegerField(blank=True, null=True)
#     per_bulk_sell_rate=models.IntegerField(blank=True, null=True)
#     time=models.DateTimeField(auto_now_add=True)
#     current=models.BooleanField(default=True)

#     @staticmethod
#     def CreateBuyRate(product,bulk,per_piece_buy_rate=0,per_bulk_buy_rate=0):
#         #currentprice=productRate.objects.filter(product=product.id).latest('time')
#         #currentprice.current=False
#         #currentprice.save()
#         ProductRate.objects.create(
#             product=product,
#             per_piece_buy_rate=per_piece_buy_rate,
#             per_bulk_buy_rate=per_bulk_buy_rate
#         )
#     @staticmethod
#     def CreateSellRate(product,per_piece_sell_rate,per_bulk_rate):
#         ProductRate.objects.create(
#             product=product,
#             per_piece_sell_rate=per_piece_sell_rate,
#             per_bulk_rate=per_bulk_rate
#         )

#     @staticmethod
#     def GetCurrentPerPieceBuyRate(product):
#         current_per_piece_buy_rate=ProductRate.objects.filter(product=product.id).latest('time').per_piece_buy_rate
#         return current_per_piece_buy_rate

#     @staticmethod
#     def GetCurrentPerBulkBuyRate(product):
#         current_per_bulk_buy_rate=ProductRate.objects.filter(product=product.id).latest('time').per_bulk_buy_rate
#         return current_per_bulk_buy_rate

#     @staticmethod
#     def GetCurrentPerPieceSellRate(product):
#         current_per_piece_sell_rate=ProductRate.objects.filter(product=product.id).latest('time').per_piece_sell_rate
#         return current_per_piece_sell_rate

#     @staticmethod
#     def GetCurrentPerBulkSellRate(product):
#         current_per_bulk_sell_rate=ProductRate.objects.filter(product=product.id).latest('time').per_bulk_sell_rate
#         return current_per_bulk_sell_rate
