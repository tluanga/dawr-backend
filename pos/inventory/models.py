from django.db import models
from django.core.exceptions import ValidationError
from pos.product.models import Product, ProductCostPrice, ProductSalePrice
from pos.warehouse.models import WareHouse
from pos.supplier.models import Supplier
from pos.tax.models import GSTCode
#from pos.account.models import Invoice
from .managers import ProductSellManager
# from pos.inventory.filters import ProductStockFilter



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
    time=models.DateTimeField(auto_now_add=True)
    current=models.BooleanField(default=True)
    
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




class ProductPurchase(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productpurchase')
    warehouse=models.ForeignKey(WareHouse,on_delete=models.CASCADE, related_name='productpurchase')
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name='productpurchase')
    bulk=models.BooleanField(default=False)
    buy_rate = models.IntegerField()    
    discount=models.IntegerField(default=0)
    quantity=models.IntegerField()
    time=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(blank=True, null=True)
 
    def save(self, *args, **kwargs):
        #productStock.UpdateStock(self.product,self.quantity)
        ProductStock.UpdateStock(self.product,self.bulk,self.quantity,mode='ADD')
        ProductCostPrice.CreateBuyRate(self.product,self.bulk,self.buy_rate)
        ProductSalePrice.CreateSaleRate(self.product,self.bulk,self.buy_rate)    
        
        super(ProductPurchase, self).save(*args, **kwargs) # Call the real save() method
    

    def __str__(self):
        return str(self.product)


class SellItem(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    sell_rate = models.FloatField(null=True)
    mrp = models.IntegerField()
    cost_price = models.IntegerField()
    gst_code = models.CharField(max_length=255)
    gst_rate = models.FloatField()
    amount = models.IntegerField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField()
    quantity = models.FloatField()

    def __str__(self):
        return self.product_name

class Sell(models.Model):
    id = models.IntegerField(primary_key=True)
    invoice_no = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sell_item = models.ManyToManyField(SellItem, related_name='sell', default=None, blank=True)
    gst_no = models.CharField(max_length=255)
    total_tax = models.FloatField()
    total_discount = models.IntegerField()
    total_amount = models.IntegerField()
    date_and_time = models.DateTimeField(auto_now_add=True)
 

# class ProductSell(models.Model):  
#     sellItem=models.ForeignKey()  
#     product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productSell')     
#     bulk=models.BooleanField(default=False) 
    
    
    
    
       
    
#     sell_time=models.DateTimeField(auto_now_add=True)
    
#     tax=models.FloatField(blank=True, null=True)
#     invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='productsell')
#     objects=ProductSellManager()

#     #check for the availability of stock for available quantity
    

#     def CalculateProfit(self):
#         if self.bulk==True:
#             buy_rate=150
#             buy_amount=self.quantity*buy_rate
#             sell_rate=self.quantity*self.sell_rate
#             self.profit=buy_rate-sell_rate
#         else:
#             buy_rate=ProductRate.GetCurrentPerPieceBuyRate(self.product)
#             buy_amount=self.quantity*buy_rate
#             sell_rate=self.quantity*self.sell_rate
#             self.profit=buy_rate-sell_rate
        
    
#     def CalculateTax(self):
#         product_gst_code=self.product.gstcode
#         code=self.product.gstcode
#         Tax=GSTCode.objects.get(code=code)
#         self.tax=Tax.CalculateTax(self.sell_rate)
        
#         print(self.tax)
        
   
   
    
#     def save(self, *args, **kwargs):
#         productstock=productStock.CheckStock(self.product)
#         if productstock is None:
#             ValidationError.message('Zero Stock')
#         elif productstock<self.quantity:
#             ValidationError.message('Not Enough Quantity ')
        
#         self.CalculateTax()
        
#         productStock.UpdateStock(self.product,self.bulk,self.quantity,mode='REMOVE')
#         self.CalculateProfit()
#         print(productSell.objects.CurrentMonthlySales())
#         super(productSell, self).save(*args, **kwargs) # Call the real save() method

#     def __str__(self):
#         return str(self.product)
