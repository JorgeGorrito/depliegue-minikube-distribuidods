from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from BusRoute.models.Bus import Bus
from BusRoute.serializers.Bus import BusSerializer

class BusViewSet(ViewSet):
    queryset = Bus.objects.all()
    serializer = BusSerializer

    def list(self, request):
        bus_serializer = self.serializer(self.queryset, many=True)
        return Response(bus_serializer.data)
