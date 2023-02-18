from django.contrib import admin
from BusRoute import models as mbr
# Register your models here.
@admin.register(mbr.Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(mbr.Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('timetable', 'bus', 'busStop')

@admin.register(mbr.BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude')

@admin.register(mbr.TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'hour')