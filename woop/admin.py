from django.contrib import admin

# Register your models here.
from .models import Goal, Task

class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Goal, GoalAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'goal', 'id')
    ordering = ('-created_at',)
    readonly_field = ('id', 'created_at')

admin.site.register(Task, TaskAdmin)
