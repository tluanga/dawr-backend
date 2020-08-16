from django.db import models


class WareHouse(models.Model):
    name = models.CharField(max_length=250)
    description: models.CharField(max_length=250)

    def __str__(self):
        return self.name
