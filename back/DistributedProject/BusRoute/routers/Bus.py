from rest_framework.routers import DefaultRouter
from BusRoute.views.Bus import BusViewSet

router = DefaultRouter()
router.register('', BusViewSet, basename='')
urlpatterns = router.urls