from rest_framework import routers
from restapi.views import PositionViewSet

router = routers.DefaultRouter()
router.register(r'position', PositionViewSet)