from django.urls import path, include
from rest_framework import routers
from .api import CrudViewSet

router = routers.DefaultRouter()
router.register('crud', CrudViewSet)  # endpoint: /crud/

urlpatterns = [
    path('', include(router.urls)),
]
