from rest_framework import serializers
from BusRoute.models.Bus import Bus

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'
    
    
