from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from woop.models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea, Reference, Note
from .serializers import GoalSerializer, TaskSerializer, MotiveSerializer, SelfTranscendenceGoalSerializer, FutureSelfSerializer, WorrySerializer, IdeaSerializer, ReferenceSerializer, NoteSerializer

# permission setting
from rest_framework.permissions import IsAuthenticated

# About the


#  About the Goal Model
class GoalViewSet(viewsets.ModelViewSet):
    'add "return self.queryset.filter(user=self.request.user)"'
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]  # authenticated-accessible


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class MotiveViewSet(viewsets.ModelViewSet):
    queryset = Motive.objects.all()
    serializer_class = MotiveSerializer
    permission_classes = [IsAuthenticated]


class SelfTranscendenceGoalViewSet(viewsets.ModelViewSet):
    queryset = SelfTranscendenceGoal.objects.all()
    serializer_class = SelfTranscendenceGoalSerializer
    permission_classes = [IsAuthenticated]


class FutureSelfViewSet(viewsets.ModelViewSet):
    queryset = FutureSelf.objects.all()
    serializer_class = FutureSelfSerializer
    permission_classes = [IsAuthenticated]


class WorryViewSet(viewsets.ModelViewSet):
    queryset = Worry.objects.all()
    serializer_class = WorrySerializer
    permission_classes = [IsAuthenticated]


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticated]


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


# About the Task Model
