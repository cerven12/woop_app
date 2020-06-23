from django.contrib import admin

# Register your models here.
from .models import Goal, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea, Note
from .models import Task, Reason, Feedback, Hurdle, Solution, Document, Discover


####################################
#                           Goal                                 #
####################################
class GoalAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'goal_title', 'created_at', 'goal_description',
                    'start_date', 'deadline', 'achievement', 'progress_type', 'goal_id')
    ordering = ('-created_at',)
    readonly_field = ('goal_id', 'created_at')


admin.site.register(Goal, GoalAdmin)


class MotiveAdmin(admin.ModelAdmin):
    list_display = ('motive', 'created_at', 'goal', 'motive_id')
    ordering = ('-created_at',)
    readonly_field = ('motive_id', 'created_at')


admin.site.register(Motive, MotiveAdmin)


class SelfTranscendenceGoalAdmin(admin.ModelAdmin):
    list_display = ('self_transcendence_goal',
                    'created_at', 'goal', 'selftrans_id')
    ordering = ('-created_at',)
    readonly_field = ('selftrans_id', 'created_at')


admin.site.register(SelfTranscendenceGoal, SelfTranscendenceGoalAdmin)


class FutureSelfAdmin(admin.ModelAdmin):
    list_display = ('future_self', 'created_at', 'goal', 'future_id')
    ordering = ('-created_at',)
    readonly_field = ('future_id', 'created_at')


admin.site.register(FutureSelf, FutureSelfAdmin)


class WorryAdmin(admin.ModelAdmin):
    list_display = ('worry', 'created_at', 'goal', 'worry_id')
    ordering = ('-created_at',)
    readonly_field = ('worry_id', 'created_at')


admin.site.register(Worry, WorryAdmin)


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('idea', 'created_at', 'worry', 'idea_id')
    ordering = ('-created_at',)
    readonly_field = ('idea_id', 'created_at')


admin.site.register(Idea, IdeaAdmin)


class NotesAdmin(admin.ModelAdmin):
    list_display = ('note_id', 'note_title', 'note_main', 'created_at', 'update_at',
                    'first_hint', 'second_hint', 'third_hint', 'goal')
    ordering = ('-created_at',)
    readonly_field = ('note_id', 'created_at',)


admin.site.register(Note, NotesAdmin)


####################################
#                           TASK                                 #
####################################

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'created_at', 'goal',
                    'task_id', 'is_repeat', 'backup_plan')
    ordering = ('-created_at', 'is_repeat')
    readonly_field = ('task_id', 'created_at')


admin.site.register(Task, TaskAdmin)


class ReasonAdmin(admin.ModelAdmin):
    list_displey = ('reason_id', 'reason', 'created_at', 'task')
    ordering = ('-created_at',)
    readonly_field = ('reason_id', 'created_at')


admin.site.register(Reason, ReasonAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_displey = ('feedback_id', 'feedback', 'created_at', 'task')
    ordering = ('-created_at',)
    readonly_field = ('feedback_id', 'created_at')


admin.site.register(Feedback, FeedbackAdmin)


class HurdleAdmin(admin.ModelAdmin):
    list_displey = ('hurdle_id', 'hurdle', 'created_at', 'task')
    ordering = ('-created_at',)
    readonly_field = ('hurdle_id', 'created_at')


admin.site.register(Hurdle, HurdleAdmin)


class SolutionAdmin(admin.ModelAdmin):
    list_displey = ('solution_id', 'solution', 'created_at', 'hurdle')
    ordering = ('-created_at',)
    readonly_field = ('solution_id', 'created_at')


admin.site.register(Solution, SolutionAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_displey = ('document_id', 'document_name',
                    'document_use', 'document_source', 'created_at', 'task')
    ordering = ('-created_at',)
    readonly_field = ('document_id', 'created_at')


admin.site.register(Document, DocumentAdmin)


class DiscoverAdmin(admin.ModelAdmin):
    list_displey = ('discover_id', 'discover_title',
                    'discover_main', 'created_at', 'update_at', 'first_hint', 'second_hint', 'third_hint')
    ordering = ('-created_at',)
    readonly_field = ('discover_id', 'created_at')


admin.site.register(Discover, DiscoverAdmin)
