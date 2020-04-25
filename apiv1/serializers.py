from rest_framework import serializers
from woop.models import Goal, Task
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'task_title', 'created_at', 'goal']


class GoalSerializer(WritableNestedModelSerializer):
    tasks = TaskSerializer(many=True, required=False)

    class Meta:
        model = Goal
        fields = ['id', 'goal_title','created_at','goal_description', 'start_date','deadline','achievement','progress_type', 'tasks']


