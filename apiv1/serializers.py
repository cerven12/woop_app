from rest_framework import serializers
# models
from woop.models import Goal, Task

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ['id', 'title', 'created_at']


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'goal']