from django.db import models


class Bus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural='Bus'

    def __str__(self):
        return self.name 