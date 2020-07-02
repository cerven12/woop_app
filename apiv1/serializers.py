from rest_framework import serializers
from woop.models import Goal, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea, Reference, Note
from woop.models import Task, Reason, Feedback, Hurdle, Solution, Document, Discover, Board, Step
from account.models import CustomUser
from drf_writable_nested.serializers import WritableNestedModelSerializer


####################################
#                           Task                                 #
####################################
class DiscoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discover
        fields = ['discover_id', 'discover_title', 'discover_main',
                  'created_at', 'update_at', 'first_hint', 'second_hint',
                  'third_hint', 'task']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['document_id', 'document_name', 'document_use',
                  'document_source', 'created_at', 'task']


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['solution_id', 'solution', 'created_at', 'hurdle']


class HurdleSerializer(WritableNestedModelSerializer):
    solutions = SolutionSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Hurdle
        fields = ['hurdle_id', 'hurdle', 'created_at', 'task', 'solutions']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback_id', 'feedback', 'created_at', 'task']


class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = ['reason_id', 'reason', 'created_at', 'task', ]


class TaskSerializer(WritableNestedModelSerializer):
    reasons = ReasonSerializer(many=True, required=False, allow_null=True)
    feedbacks = FeedbackSerializer(many=True, required=False, allow_null=True)
    hurdles = HurdleSerializer(many=True, required=False, allow_null=True)
    documents = DocumentSerializer(many=True, required=False, allow_null=True)
    discovers = DiscoverSerializer(many=True, required=False, allow_null=True)
    goal_title = serializers.CharField(read_only=True, source="goal.goal_title")
    board_title = serializers.CharField(read_only=True, source="board.board_title")


    class Meta:
        model = Task
        fields = ['task_id', 'task_title', 'task_description',  'criteria','created_at', 'board',
                  'board_title', 'order_by',
                  'goal', 'goal_title', 'is_repeat', 'backup_plan',
                  'reasons', 'feedbacks', 'hurdles', 'documents', 'discovers',
                  'satisfaction', 'difficulty']


class TaskSerializeForBoard(serializers.ModelSerializer):
    goal_title = serializers.CharField(read_only=True, source="goal.goal_title")
    board_title = serializers.CharField(read_only=True, source="board.board_title")

    class Meta:
        model = Task
        fields = ['task_id', 'task_title', 'task_description',  'criteria','created_at',
                  'board', 'board_title', 'step', 'order_by',
                  'goal', 'goal_title', 'is_repeat', 'backup_plan',
                  'reasons', 'feedbacks', 'hurdles', 'documents', 'discovers',
                  'satisfaction', 'difficulty']


# Unnecessary all child models of 'Task' model,  use 'TaskSerializeForBoard' return result a just 'Task' model object.
class BoardSerializerNestedJustTask(WritableNestedModelSerializer):
    # tasks = TaskSerializeForBoard(many=True, required=False, allow_null=True)
    tasks = TaskSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Board
        fields = ['board_id', 'goal', 'board_title',
                  'created_at', 'updated_at', 'order_by', 'tasks']

class TaskSerializeForStep(serializers.ModelSerializer):
    goal_title = serializers.CharField(read_only=True, source="goal.goal_title")

    class Meta:
        model = Task
        fields = ['task_id', 'task_title','task_description', 'criteria',
                  'created_at', 'board', 'step',  'order_by',
                  'goal', 'goal_title', 'is_repeat', 'backup_plan',
                  'reasons', 'feedbacks', 'hurdles', 'documents', 'discovers',
                  'satisfaction', 'difficulty']



class StepSerializerNestedJustTask(WritableNestedModelSerializer):
    tasks = TaskSerializeForStep(many=True, required=False, allow_null=True)

    class Meta:
        model = Step
        fields = ['step_id', 'goal', 'step_title', 'created_at', 'updated_at',
                  'order_by', 'is_active', 'tasks' ]

####################################
#                           Goal                                 #
####################################
class MotiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motive
        fields = ['motive_id', 'motive', 'created_at', 'goal']


class SelfTranscendenceGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfTranscendenceGoal
        fields = ['selftrans_id',
                  'self_transcendence_goal', 'created_at', 'goal']


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


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = [
            'reference_id', 'reference_name', 'reference_use',
            'reference_source', 'created_at', 'goal'
        ]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'note_id', 'note_title', 'note_main',
            'created_at', 'update_at', 'goal'
        ]


class GoalSerializer(WritableNestedModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    boards = BoardSerializerNestedJustTask(many=True, required=False)
    steps = StepSerializerNestedJustTask(many=True, required=False)
    motives = MotiveSerializer(many=True, required=False)
    self_transcendence_goals = SelfTranscendenceGoalSerializer(
        many=True, required=False)
    future_selves = FutureSelfSerializer(many=True, required=False)
    worries = WorrySerializer(many=True, required=False, allow_null=True)
    references = ReferenceSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)

    # Automatically specify the user who is logged in.
    created_by = serializers.ReadOnlyField(source='created_by.user_id')

    class Meta:
        model = Goal
        fields = [
            'goal_id', 'goal_title', 'created_by', 'created_at', 'goal_description',
            'criteria', 'start_date', 'deadline', 'achievement', 'progress_type',
            'motives', 'self_transcendence_goals', 'future_selves', 'worries',
            'references', 'notes', 'tasks', 'boards', 'steps',
        ]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'user_id']
