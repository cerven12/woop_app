from rest_framework import serializers
from woop.models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea, Reference, Note
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'task_title', 'created_at', 'goal']


class MotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motive
        fields = ['motive_id', 'motive', 'created_at', 'goal']

class SelfTranscendenceGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfTranscendenceGoal
        fields = ['selftrans_id', 'self_transcendence_goal', 'created_at', 'goal']


class FutureSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutureSelf
        fields = ['future_id', 'future_self', 'created_at', 'goal']


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['idea_id', 'idea', 'created_at', 'worry']


class WorrySerializer(WritableNestedModelSerializer):
    ideas = IdeaSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Worry
        fields = ['worry_id', 'worry', 'created_at', 'goal', 'ideas']


class ReferenceSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Reference
        fields = [
            'reference_id', 'reference_name', 'reference_use',
            'reference_source', 'created_at', 'goal'
            ]


class NoteSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Note
        fields = [
            'note_id', 'note_title', 'note_main',
            'created_at', 'update_at', 'goal'
            ]


class GoalSerializer(WritableNestedModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    motives = MotiveSerializer(many=True, required=False)
    self_transcendence_goals = SelfTranscendenceGoalSerializer(many=True, required=False)
    future_selves = FutureSelfSerializer(many=True, required=False)
    worries = WorrySerializer(many=True, required=False, allow_null=True)
    references = ReferenceSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)

    class Meta:
        model = Goal
        fields = [
            'goal_id', 'goal_title','created_at','goal_description',
            'start_date','deadline','achievement','progress_type',
            'motives', 'self_transcendence_goals', 'future_selves', 'worries',
            'references', 'notes', 'tasks'
            ]


