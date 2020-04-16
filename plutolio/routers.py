from rest_framework import routers
from plutolioapi.viewsets import PositionViewSet

router = routers.DefaultRouter()
router.register(r'position', PositionViewSet)