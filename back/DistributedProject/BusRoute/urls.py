from django.urls import path, include
from BusRoute.routers import Bus, Route, BusStop


urlpatterns = [
    path('bus/', include(Bus.router.urls)),
    path('routes/', include(Route.router.urls)),
    path('bus-stop/', include(BusStop.router.urls)), 
]