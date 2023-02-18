from django.db import models 

class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    hour = models.TimeField() 

    def __str__(self):
        return str(self.hour)