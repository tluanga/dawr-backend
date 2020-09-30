from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=250)
    address=models.TextField(blank=True, null=True)
    pin_code=models.PositiveIntegerField()
    mobile=models.PositiveIntegerField(blank=True, null=True)
    email=models.EmailField(blank=True,null=True)
    gst_no=models.CharField(max_length=250,blank=True, null=True)
    remarks=models.TextField(blank=True, null=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name