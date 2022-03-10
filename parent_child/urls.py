from django.urls import path
from rest_framework import routers

# App views
from .views.parent_views import ParentViewSet
from .views.child_views import ChildViewSet


# ModelViewSet config
parent_child_router = routers.DefaultRouter()

# Parent & child routers
parent_child_router.register('parents', ParentViewSet, basename='parents-test')  # basename used for unit testing
parent_child_router.register('children', ChildViewSet, basename='children-test')

# APIView config
urlpatterns = []

