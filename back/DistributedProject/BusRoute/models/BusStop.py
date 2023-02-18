from django.db import models

class BusStop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=52)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
 
    class Meta:
        verbose_name_plural = 'BusStop'

    def __str__(self):
        return self.name