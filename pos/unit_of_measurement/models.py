from django.db import models

class UnitOfMeasurement(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    measurement_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name