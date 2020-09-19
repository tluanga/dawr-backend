from django.db import models

class CustomerType(models.Model):
    name = models.CharField(max_length=250)
    discount_percentage=models.IntegerField()
    remarks=models.TextField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    customer_type=models.ForeignKey(CustomerType,on_delete=models.DO_NOTHING, related_name='customers')
    name = models.CharField(max_length=50,blank=True, null=True)
    address1=models.CharField(max_length=250,blank=True, null=True)
    city=models.CharField(max_length=250,blank=True, null=True)
    contact_no=models.PositiveIntegerField()
    email=models.EmailField(blank=True, null=True)
    gst_no=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
