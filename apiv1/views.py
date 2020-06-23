from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from woop.models import Goal, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea, Reference, Note
from .serializers import GoalSerializer, TaskSerializer, MotiveSerializer, SelfTranscendenceGoalSerializer, \
    FutureSelfSerializer, WorrySerializer, IdeaSerializer, ReferenceSerializer, NoteSerializer
# permission setting

from woop.models import Task, Reason, Feedback, Solution, Hurdle, Document, Discover
from .serializers import TaskSerializer, ReasonSerializer, FeedbackSerializer, SolutionSerializer, \
        HurdleSerializer, DocumentSerializer, DiscoverSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin


#  About the Goal Model
class GoalViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    'add "return self.queryset.filter(user=self.request.user)"'
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    # Automatically specify the user who is logged in.
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    # Filtering the user who is logged in.
    def get_queryset(self):
        return Goal.objects.filter(created_by=self.request.user)


class MotiveViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Motive.objects.all()
    serializer_class = MotiveSerializer
    permission_classes = [IsAuthenticated]


class SelfTranscendenceGoalViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = SelfTranscendenceGoal.objects.all()
    serializer_class = SelfTranscendenceGoalSerializer
    permission_classes = [IsAuthenticated]


class FutureSelfViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = FutureSelf.objects.all()
    serializer_class = FutureSelfSerializer
    permission_classes = [IsAuthenticated]


class WorryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Worry.objects.all()
    serializer_class = WorrySerializer
    permission_classes = [IsAuthenticated]


class IdeaViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]


class ReferenceViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticated]


class NoteViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


# About the Task Model
class TaskViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class ReasonViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
    permission_classes = [IsAuthenticated]

class FeedbackViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

class HurdleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Hurdle.objects.all()
    serializer_class =HurdleSerializer
    permission_classes = [IsAuthenticated]

class SolutionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [IsAuthenticated]

class DocumentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

class DiscoverViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer
    permission_classes = [IsAuthenticated]

