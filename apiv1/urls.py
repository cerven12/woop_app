from django.urls import path, include
from rest_framework_nested import routers
# from rest_framework import routers
from apiv1 import views


# router = routers.DefaultRouter()
# router.register('Goal', views.GoalViewSet)


router = routers.DefaultRouter()
router.register('goals', views.GoalViewSet)
goals_router = routers.NestedSimpleRouter(router, 'goals')
goals_router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(goals_router.urls)),
]

