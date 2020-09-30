from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    abbreviation=models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    description=models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.name
