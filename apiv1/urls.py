from django.urls import path, include
from rest_framework_nested import routers
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('Goal', views.GoalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

