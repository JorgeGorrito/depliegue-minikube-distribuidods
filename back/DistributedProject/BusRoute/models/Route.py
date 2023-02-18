from django.db import models
from BusRoute.models.Bus import Bus
from BusRoute.models.BusStop import BusStop
from BusRoute.models.TimeTable import TimeTable
 
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    busStop = models.ForeignKey(BusStop, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Routes'

    def __str__(self) -> str:
        return f'bus: {self.bus.name} - hora: {self.timetable.hour} - busStop: {self.busStop.name}'
