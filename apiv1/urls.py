from django.urls import path, include
from apiv1 import views
from rest_framework.routers import DefaultRouter

from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_extensions.routers import NestedRouterMixin


class NestedRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedRouter()

goals_routes = router.register(r'goals', views.GoalViewSet, basename='goals')

# Tasks
goals_routes.register(
    r'tasks',
    views.TaskViewSet,
    basename='tasks',
    parents_query_lookups=['goal']
)

# Motives
goals_routes.register(
    r'motives',
    views.MotiveViewSet,
    basename='motives',
    parents_query_lookups=['goal']
)

# Self Transcendence
goals_routes.register(
    r'self_transcendence_goals',
    views.SelfTranscendenceGoalViewSet,
    basename='self_transcendence_goals',
    parents_query_lookups=['goal']
)

# Future Selves
goals_routes.register(
    r'future_selves',
    views.FutureSelfViewSet,
    basename='future_selves',
    parents_query_lookups=['goal']
)

# Worries
goals_routes.register(
    r'worries',
    views.WorryViewSet,
    basename='worries',
    parents_query_lookups=['goal']
# Ideas
).register(
    'ideas',
    views.IdeaViewSet,
    basename='ideas',
    parents_query_lookups=['worry__goal', 'worry']
)

# References
goals_routes.register(
    r'references',
    views.ReferenceViewSet,
    basename='references',
    parents_query_lookups=['goal']
)

# Notes
goals_routes.register(
    r'notes',
    views.NoteViewSet,
    basename='notes',
    parents_query_lookups=['goal']
)

urlpatterns = router.urls
