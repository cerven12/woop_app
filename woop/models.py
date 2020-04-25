from django.db import models
from django.utils import timezone

# Create your models here.
import uuid


class Goal(models.Model):
    progress_type_choice = (
        (0, '一時停止'),
        (1, '挑戦中'),
        (2, '達成済'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goal_title = models.CharField(verbose_name='目標', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)
    goal_description = models.TextField(verbose_name='詳細', blank=True, null=True)
    start_date = models.DateField(verbose_name='開始日', blank=True, null=True)
    deadline = models.DateField(verbose_name='締め切り', blank=True, null=True)
    achievement = models.IntegerField(verbose_name='達成度', null=True, blank=True)
    progress_type = models.IntegerField(verbose_name='進捗状況', choices=progress_type_choice, null=True, blank=True)

    def __str__(self):
        return self.goal_title


class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='tasks')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_title = models.CharField(verbose_name='やること', max_length=40)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_title