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
    goal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_title = models.CharField(verbose_name='やること', max_length=40)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_title


class Motive(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='motives')
    motive_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    motive = models.TextField(verbose_name='動機', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)

    def __str__(self):
        return self.motive


class SelfTranscendenceGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='self_transcendence_goals')
    selftrans_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    self_transcendence_goal = models.TextField(verbose_name='自己超越目標', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)

    def __str__(self):
        return self.self_transcendence_goal or ''


class FutureSelf(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='future_selves')
    future_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    future_self = models.TextField(verbose_name='将来の自分', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)

    def __str__(self):
        return self.future_self or ''


class Worry(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='worries')
    worry_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    worry = models.TextField(verbose_name='心配事', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)

    def __str__(self):
        return self.worry or ''


class Idea(models.Model):
    worry = models.ForeignKey(Worry, on_delete=models.CASCADE, related_name='ideas')
    idea_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idea = models.TextField(verbose_name='対策', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)

    def __str__(self):
        return self.idea or ''


class Reference(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='references')
    reference_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference_name = models.CharField(verbose_name='資料', null=True, blank=True, max_length=200)
    reference_use = models.CharField(verbose_name='用途', null=True, blank=True, max_length=200)
    reference_source = models.URLField(verbose_name='場所', null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)

    def __str__(self):
        return self.reference_name or ''


class Note(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='notes')
    note_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note_title = models.CharField(verbose_name='タイトル', null=True, blank=True, max_length=200)
    note_main = models.TextField(verbose_name='本文', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時' ,default=timezone.now)
    update_at = models.DateTimeField(verbose_name='更新日時' ,default=timezone.now)

    def __str__(self):
        return self.note_title or ''