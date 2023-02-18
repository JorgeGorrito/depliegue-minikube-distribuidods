from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from BusRoute.models.BusStop import BusStop
from BusRoute.serializers.BusStop import BusStopSerializer

class BusStopViewSet(ViewSet):
    queryset = BusStop.objects.all()
    serializer = BusStopSerializer

    def list(self, request):
        busStop_serializer = self.serializer(self.queryset, many=True)
        return Response(busStop_serializer.data)