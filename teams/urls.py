from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
