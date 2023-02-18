from rest_framework.routers import DefaultRouter
from BusRoute.views.Route import RouteViewSet

router = DefaultRouter()
router.register('', RouteViewSet, basename='')
urlpatterns = router.urls