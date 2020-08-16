from django.db import models
from django.core.exceptions import ValidationError
from pos.product.models import Product
from pos.inventory.models import ProductStock
from pos.product.models import GSTCode

# Create your models here.


    

class Order(models.Model):
    ref_code = models.CharField(max_length=255)
    total = models.FloatField()
    discount = models.IntegerField(default=0)
    totalTax = models.FloatField(blank=True, null=True)
    cash_received=models.IntegerField()    
    cash_rounded_off = models.IntegerField(default=0)
    returned=models.IntegerField()    
    remarks = models.TextField(blank=True, null=True)
    
    
    #objects=ProductSellManager()
    def CalculateTax(self):
        #add all the tax of order items
        orderitems = OrderItem.objects.filter(order=self)
        print(str(orderitems))
        
    
    def get_cart_items(self):
        return self.items

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
    
    def __str__(self):
        return str(self.ref_code)
    
    def CalculateProfit(self):
        if self.bulk==True:
            buy_rate=150
            buy_amount=self.quantity*buy_rate
            sell_rate=self.quantity*self.sell_rate
            self.profit=buy_rate-sell_rate
        else:
            buy_rate=ProductRate.GetCurrentPerPieceBuyRate(self.product)
            buy_amount=self.quantity*buy_rate
            sell_rate=self.quantity*self.sell_rate
            self.profit = buy_rate - sell_rate
            

    def save(self, *args, **kwargs):
       self.CalculateTax()
       super(Order, self).save(*args, **kwargs) # Call the real save() method

class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='orderItem')
    quantity = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now=True)
    sell_rate = models.IntegerField()
    profit = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderItem')
    tax=models.FloatField(blank=True, null=True)
    # def clean(self):
    #     if self.product.quantity==0:
    #         raise ValidationError('Zero Quantity')

    # def __str__(self):
    #     return str(self.product)

    # def save(self, *args, **kwargs):
    #     productstock = ProductStock.CheckStock(self.product)
    #     print(str(productstock))
    #     if productstock is None:
    #         ValidationError.message('Zero Stock')
    #     elif productstock<self.quantity:
    #         ValidationError.message('Not Enough Quantity ')

    #     self.CalculateTax()

        # productStock.UpdateStock(self.product,self.bulk,self.quantity,mode='REMOVE')
        # self.CalculateProfit()
        # print(productSell.objects.CurrentMonthlySales())
        # super(productSell, self).save(*args, **kwargs) # Call the real save() method
    def CalculateTax(self):
        product_gst_code = self.product.gstcode
        code = self.product.gstcode
        Tax = GSTCode.objects.get(code=code)
        self.tax = Tax.CalculateTax(self.sell_rate)

        print(self.tax)

    def __str__(self):
        return str(self.product)
