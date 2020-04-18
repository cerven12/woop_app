from django.shortcuts import render
from rest_framework import viewsets
# models
from woop.models import Goal, Task
from .serializers import GoalSerializer, TaskSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer