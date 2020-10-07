from django.db import models

class UnitOfMeasurement(models.Model):
    active = models.BooleanField(default=True)
    unit_of_measurement = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    type_of_measurement=models.CharField(max_length=255)
    

    def __str__(self):
        return self.name