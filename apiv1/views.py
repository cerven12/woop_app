from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from woop.models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry , Idea, Reference, Note
from .serializers import GoalSerializer, TaskSerializer, MotiveSerializer, SelfTranscendenceGoalSerializer, FutureSelfSerializer, WorrySerializer, IdeaSerializer, ReferenceSerializer, NoteSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    # def list(self, request,):
    #     queryset = Goal.objects.filter()
    #     serializer = GoalSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Goal.objects.filter()
    #     goal = generics.get_object_or_404(queryset, pk=pk)
    #     serializer = GoalSerializer(goal)
    #     return Response(serializer.data)


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


class WorryViewSet(viewsets.ModelViewSet):
    queryset = Worry.objects.all()
    serializer_class = WorrySerializer

    # def list(self, request, goal_pk=None):
    #     queryset = Worry.objects.filter(goal_id=goal_pk)
    #     serializer = WorrySerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None, goal_pk=None):
    #     queryset = Worry.objects.filter(pk=pk, goal_id=goal_pk)
    #     worry = generics.get_object_or_404(queryset, pk=pk)
    #     serializer = WorrySerializer(worry)
    #     return Response(serializer.data)


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    # def list(self, request, goal_pk=None, worry_pk=None):
    #     queryset = Idea.objects.filter(worry_id__goal_id=goal_pk, worry_id=worry_pk)
    #     serializer = IdeaSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None, goal_pk=None, worry_pk=None):
    #     queryset = Idea.objects.filter(pk=pk, worry_id__goal_id=goal_pk, worry_id=worry_pk)
    #     idea = generics.get_object_or_404(queryset, pk=pk)
    #     serializer = IdeaSerializer(idea)
    #     return Response(serializer.data)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer