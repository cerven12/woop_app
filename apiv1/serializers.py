from rest_framework import serializers
from woop.models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'task_title', 'created_at', 'goal']


class MotiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Motive
        fields = ['id', 'motive', 'created_at', 'goal']

class SelfTranscendenceGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SelfTranscendenceGoal
        fields = ['id', 'self_transcendence_goal', 'created_at', 'goal']

class FutureSelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = FutureSelf
        fields = ['id', 'future_self', 'created_at', 'goal']

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worry
        fields = ['id', 'idea', 'created_at', 'worry']


class WorrySerializer(WritableNestedModelSerializer):
    ideas = IdeaSerializer(many=True, required=False)

    class Meta:
        model = Worry
        fields = ['id', 'worry', 'created_at', 'goal', 'ideas']


class GoalSerializer(WritableNestedModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    motives = MotiveSerializer(many=True, required=False)
    self_transcendence_goals = SelfTranscendenceGoalSerializer(many=True, required=False)
    future_selves = FutureSelfSerializer(many=True, required=False)
    worries = WorrySerializer(many=True, required=False)

    class Meta:
        model = Goal
        fields = ['id', 'goal_title','created_at','goal_description',
        'start_date','deadline','achievement','progress_type',
        'motives', 'self_transcendence_goals', 'future_selves', 'worries', 'tasks']


