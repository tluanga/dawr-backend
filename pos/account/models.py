from django.db import models
from django.utils import dates
from pos.product.models import Product

# class CartItem(models.Model):
#     item=models.ManyToManyField(Product, on_delete=models.SET_NULL)
#     is_ordered=models.BooleanField(default=False)
#     date_added=models.DateTimeField(auto_now=True)
#     data_ordered=models.DateTimeField(null=True)


# class Cart(models.Model):
#     ref_code=models.CharField(max_length=255)
#     is_ordered=models.BooleanField(default=False)
#     items=models.ManyToManyField(CartItem)
#     purchase_time=models.DateTimeField(auto_now=True)

#     def get_cart_items(self):
#         return self.items.all()

#     def get_cart_total(self):
#         return sum([item.product.price for item in self.items.all()])

# class Invoice(models.Model):
#     invoice_number=models.IntegerField()
#     date= models.DateField(auto_now=True)
#     taxable_amount=models.FloatField()
#     total_tax=models.FloatField()
#     invoice_total=models.FloatField()
        


#     def __str__(self):
#         return str(self.invoice_number)

# #create an sellpage
# #from the sellpage select an item
# #  
