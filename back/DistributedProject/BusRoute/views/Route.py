from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import datetime
from BusRoute.pagination.Custom import CustomPagination
from BusRoute.models.Route import Route, BusStop, Bus, TimeTable
from BusRoute.serializers.Route import RouteSerializer
from BusRoute.models.TimeTable import TimeTable

class RouteViewSet(ViewSet):
    pagination_class = CustomPagination
    queryset = Route.objects.all()
    serializer = RouteSerializer

    def list(self, request):
        route_serializer = self.serializer(self.queryset, many=True)
        return Response(route_serializer.data)

        
    @action(detail=False, methods=['get'], url_path='nextRoute')   
    def nextRoute(self, request):
        bus_name = request.GET.get('bus', None)
        hrs = request.GET.get('hour', None)
        
        if hrs and bus_name: 
            hora = datetime.datetime.strptime(hrs, '%H:%M:%S').time()
            nextHour = TimeTable.objects.filter(hour__gte=hora).order_by('hour').first()
            if nextHour:
                print(f'bus_name:{bus_name}.')
                try:
                    nextRoute = Route.objects.get(Q(timetable=nextHour) & Q(busStop=BusStop.objects.get(name=bus_name)))
                    route_serializer = RouteSerializer(nextRoute, many=False)
                    return Response(route_serializer.data)
                except Route.DoesNotExist:
                    return Response({'msg':'No se encontro ruta'}, status=status.HTTP_404_NOT_FOUND)
                except BusStop.DoesNotExist:
                    return Response({'msg':'No se encontro paradero'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'msg':'No se encontro hora'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status. HTTP_400_BAD_REQUEST)