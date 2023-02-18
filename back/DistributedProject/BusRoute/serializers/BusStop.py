from rest_framework.serializers import ModelSerializer
from BusRoute.models.BusStop import BusStop

class BusStopSerializer(ModelSerializer):
    class Meta:
        model = BusStop
        fields = '__all__'