from django.db import models


class GSTCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    cgst=models.FloatField()
    sgst = models.FloatField()
    igst=models.FloatField(blank=True, null=True)
    description_of_good=models.CharField(max_length=500)
    remarks = models.CharField(max_length=250,blank=True, null=True)
    active=models.BooleanField(default=True)
    
    
    def CalculateTax(self,amount):
        tax_percentage=(self.cgst+self.sgst)
        tax=(amount/100)*tax_percentage
        return tax
        
    def save(self, *args, **kwargs):
       self.totalGst=self.cgst+self.sgst
       super(GSTCode, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.code