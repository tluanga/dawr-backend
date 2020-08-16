from django.db import models


class GSTCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    cgst=models.FloatField()
    sgst=models.FloatField()
    remarks = models.CharField(max_length=250)
    
    
    def CalculateTax(self,amount):
        tax_percentage=(self.cgst+self.sgst)
        tax=(amount/100)*tax_percentage
        return tax
        

    def __str__(self):
        return self.code