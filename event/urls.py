
from django.urls import path
from rest_framework.routers import SimpleRouter

from event.views import UserViewSet, EventViewSet

# from base.script import *

router = SimpleRouter()
router.register('api/user', UserViewSet, basename='user')
router.register('api/events', EventViewSet, basename='event')

urlpatterns = router.urls