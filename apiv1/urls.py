from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('Goal', views.GoalViewSet)
router.register('Task', views.TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

