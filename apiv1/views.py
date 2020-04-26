from django.shortcuts import render
from rest_framework import viewsets
# models
from woop.models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry , Idea
from .serializers import GoalSerializer, TaskSerializer, MotiveSerializer, SelfTranscendenceGoalSerializer, FutureSelfSerializer, WorrySerializer, IdeaSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class MotiveViewSet(viewsets.ModelViewSet):
    queryset = Motive.objects.all()
    serializer_class = MotiveSerializer

class SelfTranscendenceGoalViewSet(viewsets.ModelViewSet):
    queryset = SelfTranscendenceGoal.objects.all()
    serializer_class = SelfTranscendenceGoalSerializer

class FutureSelfViewSet(viewsets.ModelViewSet):
    queryset = FutureSelf.objects.all()
    serializer_class = FutureSelfSerializer

class WorrySelfViewSet(viewsets.ModelViewSet):
    queryset = Worry.objects.all()
    serializer_class = WorrySerializer

class IdeaSelfViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer