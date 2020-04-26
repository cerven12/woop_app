from django.contrib import admin

# Register your models here.
from .models import Goal, Task, Motive, SelfTranscendenceGoal, FutureSelf, Worry, Idea

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_title','created_at','goal_description', 'start_date','deadline','achievement','progress_type','id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Goal, GoalAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'created_at', 'goal', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Task, TaskAdmin)


class MotiveAdmin(admin.ModelAdmin):
    list_display = ('motive', 'created_at', 'goal', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Motive, MotiveAdmin)


class SelfTranscendenceGoalAdmin(admin.ModelAdmin):
    list_display = ('self_transcendence_goal', 'created_at', 'goal', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(SelfTranscendenceGoal, SelfTranscendenceGoalAdmin)

class FutureSelfAdmin(admin.ModelAdmin):
    list_display = ('future_self', 'created_at', 'goal', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(FutureSelf, FutureSelfAdmin)


class WorryAdmin(admin.ModelAdmin):
    list_display = ('worry', 'created_at', 'goal', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Worry, WorryAdmin)


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('idea', 'created_at', 'worry', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Idea, IdeaAdmin)