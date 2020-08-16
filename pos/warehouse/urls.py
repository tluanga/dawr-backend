from rest_framework import routers
from .views import WareHouseViewSet

router = routers.DefaultRouter()
router.register('warehouse',WareHouseViewSet)

urlpatterns = router.urls
