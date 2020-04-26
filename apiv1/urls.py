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
goals_router.register('motives', views.MotiveViewSet)
goals_router.register('self_transcendence_goals', views.SelfTranscendenceGoalViewSet)
goals_router.register('future_selves', views.FutureSelfViewSet)
goals_router.register('worries', views.WorrySelfViewSet)

worries_router = routers.NestedSimpleRouter(goals_router, 'worries')
worries_router.register('ideas', views.IdeaSerializer)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(goals_router.urls)),
    path('', include(worries_router.urls)),
]

