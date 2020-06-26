from django.urls import path, include
from apiv1 import views
from rest_framework.routers import DefaultRouter

from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_extensions.routers import NestedRouterMixin


class NestedRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedRouter()

# Goal
goals_routes = router.register(r'goals', views.GoalViewSet, basename='goals')


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
).register(  # Ideas
    r'ideas',
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


# Tasks
tasks_routes = goals_routes.register(
    r'tasks',
    views.TaskViewSet,
    basename='tasks',
    parents_query_lookups=['goal']
)

# Boards
goals_routes.register(
    r'boards',
    views.BoardViewSet,
    basename='boards',
    parents_query_lookups=['goal']
).register(
    r'tasks',
    views.TaskViewSet,
    basename='tasks',
    parents_query_lookups=['board__goal', 'board']
)

# Steps
goals_routes.register(
    r'steps',
    views.StepViewSet,
    basename='steps',
    parents_query_lookups=['goal']
).register(
    r'tasks',
    views.TaskViewSet,
    basename='tasks',
    parents_query_lookups=['step__goal', 'step']
)


# Reasons
tasks_routes.register(
    r'reasons',
    views.ReasonViewSet,
    basename='reasons',
    parents_query_lookups=['task__goal', 'task']
)

# Feedbacks
tasks_routes.register(
    r'feedbacks',
    views.FeedbackViewSet,
    basename='feedbacks',
    parents_query_lookups=['task__goal', 'task']
)

# Hurdles
tasks_routes.register(
    r'hurdles',
    views.HurdleViewSet,
    basename='hurdles',
    parents_query_lookups=['task__goal', 'task']
).register(  # Solutions
    r'solutions',
    views.SolutionViewSet,
    basename='solutions',
    parents_query_lookups=['hurdle__task__goal', 'hurdle__task', 'hurdle']
)

tasks_routes.register(
    r'documents',
    views.DocumentViewSet,
    basename='documents',
    parents_query_lookups=['task__goal', 'task']
)

tasks_routes.register(
    r'discovers',
    views.DiscoverViewSet,
    basename='discovers',
    parents_query_lookups=['task__goal', 'task']
)


urlpatterns = router.urls
