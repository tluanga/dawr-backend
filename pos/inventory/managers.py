from django.db import models
from pos.tax.models import GSTCode

from datetime import date

class ProductSellQuerySet(models.QuerySet):
    
    def currentmonthlysales(self):
        today=date.today()
        #get sales for current month
        return self.filter(sell_time__month=today.month)
    
    def currentyearsales(self):
        today=date.today()
        return self.filter(sell_time__year=today.year)
    
    def productcurrentmonthsales(self,id):
        today=date.today()
        return self.filter(sell_time__year=today.month,product=id)

    


        '''
        Reference
        from datetime import date
        today = date.today()
        today_filter =  MyModel.objects.filter(post_date__year=today.year,
                                       post_date__month=today.month,
                                       post_date__day=today.day)'''
class ProductSellManager(models.Manager):
    
    def get_queryset(self):
        return ProductSellQuerySet(self.model, using=self._db)        
    #product sold in a month for all products
    def CurrentMonthlySales(self):
        return self.get_queryset().currentmonthlysales()
    
    def CurrentYearSales(self):
        return self.get_queryset().currentyearsales()
    
    def ProductCurrentMonthSales(self,id):
        return self.get_queryset().productcurrentmonthsales(id)
    
    

        
        #today=date.today()
        #get sales for current month
        #return self.filter(sell_date__month=today.month)
