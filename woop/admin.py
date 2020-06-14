from django.contrib import admin

# Register your models here.
from .models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea, Note

class GoalAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'goal_title','created_at','goal_description', 'start_date','deadline','achievement','progress_type','goal_id')
    ordering = ('-created_at',)
    readonly_field = ('goal_id', 'created_at')

admin.site.register(Goal, GoalAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'created_at', 'goal', 'task_id', 'is_repeat', 'backup_plan')
    ordering = ('-created_at','is_repeat')
    readonly_field = ('task_id', 'created_at')

admin.site.register(Task, TaskAdmin)


class MotiveAdmin(admin.ModelAdmin):
    list_display = ('motive', 'created_at', 'goal', 'motive_id')
    ordering = ('-created_at',)
    readonly_field = ('motive_id', 'created_at')

admin.site.register(Motive, MotiveAdmin)


class SelfTranscendenceGoalAdmin(admin.ModelAdmin):
    list_display = ('self_transcendence_goal', 'created_at', 'goal', 'selftrans_id')
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
