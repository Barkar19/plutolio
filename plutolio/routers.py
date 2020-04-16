from rest_framework import routers
from plutolioweb.viewsets import PositionViewSet

router = routers.DefaultRouter()
router.register(r'position', PositionViewSet)