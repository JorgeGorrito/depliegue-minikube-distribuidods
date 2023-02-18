from rest_framework import serializers
from BusRoute.models.Route import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.bus.id,
            'name': instance.bus.name,
            'hour': str(instance.timetable),
            'busStop':{
                'name': instance.busStop.name,
                'lat':instance.busStop.latitude,
                'lng':instance.busStop.longitude
            }
        }