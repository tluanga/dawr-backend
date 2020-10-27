from django.db import models
from django.core.exceptions import ValidationError
from pos.product.models import (Product, ProductCostPrice, ProductSellPrice)
from pos.warehouse.models import WareHouse
from pos.supplier.models import Supplier
from pos.tax.models import GSTCode
from pos.customer.models import Customer
#from pos.account.models import Invoice
from .managers import ProductSellManager

# from pos.transaction.filters import ProductStockFilter



#####TRANSACTION SIDE##############
#when ever a new product is purchased, the stock quantity will be updated
#create a model method to return number of stock

class ProductStock(models.Model):
    product_STOCK_TYPE_CHOICES = (
        ('Box','box'),
        ('Bundle','bundle')
    )
    
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productstock')
    quantity= models.IntegerField()
    stock_type=models.CharField(choices=product_STOCK_TYPE_CHOICES,max_length=100)
    bulkmode=models.BooleanField(default=False)
    retailmode=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    
    @staticmethod
    def CheckStock(product):
        currentstock=ProductStock.objects.filter(product=product.id).latest('time').quantity
        
        if currentstock>0:
            return currentstock
        else:
            return None
        

    
    @staticmethod  
    def UpdateStock(product,bulk,quantity,mode):
        try:
            currentstockobj=ProductStock.objects.filter(product=product.id).latest('time')
            currentstockobj.current=False
            currentstockobj.save()
            if mode=='ADD':
                productstock=ProductStock.objects.create(
                    product=product,
                    quantity=quantity+currentstockobj.quantity,
                    current=True)
                return productstock
            elif mode=='REMOVE':
                productstock=ProductStock.objects.create(
                    product=product, 
                    quantity=currentstockobj.quantity-quantity,
                    current=True)
                return productstock


        except ProductStock.DoesNotExist:
            if mode=='ADD':                
                productstock=ProductStock.objects.create(
                    product=product,quantity=quantity,current=True)
                return productstock
            elif mode=='REMOVE':
                return None

    def __str__(self):
        return str(self.product)

#----------Purchase Order--------
class ModeOfSell(models.Model):
    name=models.CharField(max_length=255)
    remarks=models.CharField(max_length=555, blank=True, null=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):    
    ref_no=models.CharField(max_length=255)
    # total_tax=models.FloatField(blank=True, null=True)
    # total_discount=models.FloatField(blank=True, null=True)
    # total_amount=models.FloatField()
    # date=models.DateTimeField(auto_now_add=True)
    # remarks = models.TextField(blank=True, null=True)
    # warehouse=models.ForeignKey(WareHouse,on_delete=models.CASCADE, related_name='productpurchase')
    # supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name='productpurchase')

class PurchaseOrderItem(models.Model):
    purchase_order=models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE, related_name='purchase_order_item')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productpurchase')    
    # bulk=models.BooleanField(default=False)
    # cost_price = models.FloatField()
    # cost_price_bulk=models.FloatField(blank=True, null=True)
    # sell_price=models.FloatField()
    # sell_price_bulk=models.FloatField(blank=True, null=True) 
    # discount=models.IntegerField(blank=True, null=True)
    # quantity=models.IntegerField()    
    # active=models.BooleanField(default=True)
 
    # def save(self, *args, **kwargs):
    #     if self.cost_price_bulk==None:
    #         self.cost_price_bulk=self.cost_price
    #     if self.sell_price_bulk==None:
    #         self.cost_price_bulk=self.cost_price
    #     ProductStock.UpdateStock(self.product,self.bulk,self.quantity,mode='ADD')
    #     ProductCostPrice.CreateCostPrice(self.product,self.bulk,self.cost_price)
    #     ProductSellPrice.CreateSellPrice(self.product,self.bulk,self.cost_price)    
        
    #     super(PurchaseOrderItem, self).save(*args, **kwargs) # Call the real save() method
    

    def __str__(self):
        return str(self.product)

class SettlePurchaseBill(models.Model):
    purchase_order=models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE, related_name='settle_purchase_bill')
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)
    payment_mode=models.CharField(max_length=255,blank=True, null=True)
    payment_amount=models.IntegerField(blank=True, null=True)
    remarks = models.TextField()
    active = models.BooleanField(default=True)


#######-----Sell order----#########
class SellOrder(models.Model):
    # ref_code is the invoice number we need a pattern generator
    ref_code = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now=True)
    total_discount = models.IntegerField(default=0)
    total_tax = models.FloatField(blank=True, null=True)
    total_amount=models.FloatField()       
    credit = models.BooleanField(default=False)        
    remarks = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='order')
    active=models.BooleanField(default=True)
    
    
    #objects=ProductSellManager()
    def CalculateTax(self):
        #add all the tax of order items
        orderitems = OrderItem.objects.filter(order=self)
        print(str(orderitems))
        
    
   

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
    
    def ref_code_generator(self):
        return ('A-3')

    def __str__(self):
        return str(self.ref_code)

    def save(self, *args, **kwargs):
       self.CalculateTax()
       
       super(SellOrder, self).save(*args, **kwargs) # Call the real save() method

class SellOrderItem(models.Model):
    order = models.ForeignKey(
        SellOrder, on_delete=models.CASCADE, related_name='orderItem')
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='orderItem')
    quantity = models.IntegerField()    
    discount=models.FloatField(blank=True, null=True)
    sell_price = models.IntegerField()       
    tax_code=models.CharField(max_length=255,blank=True, null=True)
    tax_price=models.FloatField(blank=True, null=True) 
    amount = models.FloatField()
    active = models.BooleanField(default=True)

    def CalculateTax(self):
        product_gst_code = self.product.gstcode
        code = self.product.gstcode
        Tax = GSTCode.objects.get(code=code)
        self.tax = Tax.CalculateTax(self.sell_price)

        print(self.tax)

    def __str__(self):
        return str(self.product)


# ---use Signals to automatically create when the order is created
# use post save signals
class SettleSellBill(models.Model):
    order=models.OneToOneField(SellOrder, on_delete=models.CASCADE,related_name='settle_sell_bill')
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)
    payment_mode=models.CharField(max_length=255,blank=True, null=True)
    payment_amount=models.IntegerField(blank=True, null=True)
    remarks = models.TextField()
    active = models.BooleanField(default=True)