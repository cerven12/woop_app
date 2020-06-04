from django.urls import path, include
from rest_framework_nested import routers
from apiv1 import views


router = routers.DefaultRouter()
router.register(r'goals', views.GoalViewSet, basename='goals')

goals_router = routers.NestedSimpleRouter(router, r'goals', lookup='goal')
goals_router.register(r'tasks', views.TaskViewSet, basename='tasks')
goals_router.register(r'motives', views.MotiveViewSet, basename='motives')
goals_router.register(r'self_transcendence_goals', views.SelfTranscendenceGoalViewSet, basename='self_transcendence_goals')
goals_router.register(r'future_selves', views.FutureSelfViewSet, basename='future_selves')
goals_router.register(r'worries', views.WorryViewSet, basename='worries')
goals_router.register(r'references', views.ReferenceViewSet, basename='references')
goals_router.register(r'notes', views.NoteViewSet, basename='notes')

worries_router = routers.NestedSimpleRouter(goals_router, r'worries', lookup='worry')
worries_router.register(r'ideas', views.IdeaViewSet, basename='ideas')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(goals_router.urls)),
    path('', include(worries_router.urls)),
]

