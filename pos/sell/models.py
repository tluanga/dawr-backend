from django.db import models
from django.core.exceptions import ValidationError
from pos.product.models import Product
from pos.inventory.models import ProductStock
from pos.product.models import GSTCode
from pos.customer.models import Customer

# Create your models here.
class ModeOfSell(models.Model):
    name=models.CharField(max_length=255)
    remarks=models.CharField(max_length=555, blank=True, null=True)

    def __str__(self):
        return self.name

    

class Order(models.Model):
    ref_code = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now=True)
    total_discount = models.IntegerField(default=0)
    total_tax = models.FloatField(blank=True, null=True)
    total_amount=models.FloatField()
    cash_received=models.IntegerField()    
    mode = models.ForeignKey(ModeOfSell,on_delete=models.DO_NOTHING,related_name='order')          
    remarks = models.TextField(blank=True, null=True)
    customer=models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='order')
    
    
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
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderItem')
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='orderItem')
    quantity = models.IntegerField()    
    discount=models.FloatField(blank=True, null=True)
    sell_rate = models.IntegerField()       
    tax_code=models.CharField(max_length=255,blank=True, null=True)
    tax_rate=models.FloatField(blank=True, null=True) 
    amount=models.FloatField()
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


class SettleBill(models.Model):
    order=models.OneToOneField(Order, on_delete=models.CASCADE,related_name='settle_bill')
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)
    payment_mode=models.CharField(max_length=255,blank=True, null=True)
    payment_amount=models.IntegerField(blank=True, null=True)
    remarks=models.TextField()
