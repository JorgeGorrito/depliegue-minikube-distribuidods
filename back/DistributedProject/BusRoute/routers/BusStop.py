from rest_framework.routers import DefaultRouter
from BusRoute.views.BusStop import BusStopViewSet

router = DefaultRouter()
router.register('', BusStopViewSet, basename='')
urlpatterns = router.urls