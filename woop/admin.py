from django.contrib import admin

# Register your models here.
from .models import Goal, Task

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
