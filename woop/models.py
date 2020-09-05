from django.db import models
from django.utils import timezone
from accounts.models import *


# Create your models here.
import uuid

# Gift is will be given immediately.


class Gift(models.Model):
    gift_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    gift = models.CharField(verbose_name='ご褒美', max_length=150)


####################################
#                           Goal                                 #
####################################
class Goal(models.Model):
    progress_type_choice = (
        (0, '一時停止'),
        (1, '挑戦中'),
        (2, '達成済'),
    )
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name='ユーザー')
    goal_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    goal_title = models.CharField(verbose_name='目標', max_length=200)
    criteria = models.TextField(
        verbose_name='成功基準', blank=True, null=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)
    goal_description = models.TextField(
        verbose_name='詳細', blank=True, null=True)
    start_date = models.DateField(verbose_name='開始日', blank=True, null=True)
    deadline = models.DateField(verbose_name='締め切り', blank=True, null=True)
    achievement = models.IntegerField(
        verbose_name='達成度', null=True, blank=True)
    progress_type = models.IntegerField(
        verbose_name='進捗状況', choices=progress_type_choice, null=True, blank=True)

    def __str__(self):
        return self.goal_title or ''


# board
class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='boards')
    board_title = models.CharField(verbose_name='ボード', max_length=255)
    color = models.CharField(verbose_name="色", max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_by = models.IntegerField(default=0)

    def __str__(self):
        return self.board_title or ''


# step
class Step(models.Model):
    step_id = models.AutoField(primary_key=True)
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='steps')
    step_title = models.CharField(verbose_name='ステップ', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_by = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["order_by"]

    def __str__(self):
        return self.step_title or ''


class Motive(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='motives')
    motive_id = models.AutoField(primary_key=True)
    motive = models.TextField(verbose_name='動機', blank=True, null=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.motive or ''


class SelfTranscendenceGoal(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='self_transcendence_goals')
    selftrans_id = models.AutoField(primary_key=True)
    self_transcendence_goal = models.TextField(
        verbose_name='自己超越目標', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.self_transcendence_goal or ''


class FutureSelf(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='future_selves')
    future_id = models.AutoField(primary_key=True)
    future_self = models.TextField(verbose_name='将来の自分', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.future_self or ''


class Worry(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='worries')
    worry_id = models.AutoField(primary_key=True)
    worry = models.TextField(verbose_name='心配事', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.worry or ''


class Idea(models.Model):
    worry = models.ForeignKey(
        Worry, on_delete=models.CASCADE, related_name='ideas')
    idea_id = models.AutoField(primary_key=True)
    idea = models.TextField(verbose_name='対策', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.idea or ''


class Reference(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='references')
    reference_id = models.AutoField(primary_key=True)
    reference_name = models.CharField(
        verbose_name='資料', null=True, blank=True, max_length=200)
    reference_use = models.CharField(
        verbose_name='用途', null=True, blank=True, max_length=200)
    reference_source = models.URLField(
        verbose_name='場所', null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.reference_name or ''


class Note(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='notes')
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(
        verbose_name='タイトル', null=True, blank=True, max_length=200)
    note_main = models.TextField(verbose_name='本文', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)
    update_at = models.DateTimeField(verbose_name='更新日時', default=timezone.now)
    first_hint = models.CharField(
        verbose_name='ヒント1', null=True, blank=True, max_length=20)
    second_hint = models.CharField(
        verbose_name='ヒント2', null=True, blank=True, max_length=20)
    third_hint = models.CharField(
        verbose_name='ヒント3', null=True, blank=True, max_length=20)

    def __str__(self):
        return self.note_title or ''


####################################
#                           TASK                                 #
####################################


class Task(models.Model):
    satisfaction_level = (
        (10, '全くない'),
        (20, 'あまりない'),
        (30, 'ほどほど'),
        (40, 'ある'),
        (50, 'かなりある'),
    )

    difficulty_level = (
        (10, 'かなり簡単'),
        (20, '簡単'),
        (30, '普通'),
        (40, '難しい'),
        (50, 'かなり難しい'),
    )

    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE, related_name='tasks')
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)
    step = models.ForeignKey(
        Step, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)
    task_id = models.AutoField(primary_key=True)
    order_by = models.IntegerField(default=0)
    task_title = models.CharField(verbose_name='やること', max_length=200)
    task_description = models.TextField(
        verbose_name='詳細', blank=True, null=True)
    criteria = models.TextField(
        verbose_name='成功基準', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_repeat = models.BooleanField(verbose_name='繰り返し', default=False)
    # Run tasks for when get stuck to main task.
    backup_plan = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    satisfaction = models.IntegerField(
        verbose_name='満足度', choices=satisfaction_level, null=True)
    difficulty = models.IntegerField(
        verbose_name='困難度', choices=difficulty_level, null=True)

    def __str__(self):
        return self.task_title or ''


class Expectation(models.Model):
    satisfaction_level = (
            (20, 20),
            (40, 40),
            (60, 60),
            (80, 80),
            (100, 100),
        )
    difficulty_level = (
            (20, 20),
            (40, 40),
            (60, 60),
            (80, 80),
            (100, 100),

        )
    task = models.ForeignKey(
            Task, on_delete=models.CASCADE, related_name='expectations')
    expectation_id = models.AutoField(primary_key=True)
    tbd_satisfaction = models.IntegerField(
            verbose_name="予想の満足度", choices=satisfaction_level, null=True, blank=True)
    tbd_satis_comment = models.CharField(
            verbose_name="満足度の予想について一言", max_length=200, null=True, blank=True)
    satisfaction = models.IntegerField(
            verbose_name="実際の満足度", choices=satisfaction_level, null=True, blank=True)
    satis_comment = models.CharField(
            verbose_name="実際の満足度について一言", max_length=200, null=True, blank=True)
    tbd_difficulty = models.IntegerField(
            verbose_name="予想の困難度", choices=difficulty_level, null=True, blank=True)
    tbd_diff_comment = models.CharField(
            verbose_name="満足度の予想について一言", max_length=200, null=True, blank=True)
    difficulty = models.IntegerField(
            verbose_name="実際の困難度", choices=difficulty_level, null=True, blank=True)
    diff_comment = models.CharField(
            verbose_name="実際の困難度について一言", max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tbd_satis_comment or ''


class Reason(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='reasons')
    reason_id = models.AutoField(primary_key=True)
    reason = models.TextField(
        verbose_name='理由', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.reason or ''


class Feedback(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.TextField(
        verbose_name='報酬', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.feedback or ''


class Hurdle(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='hurdles')
    hurdle_id = models.AutoField(primary_key=True)
    hurdle = models.TextField(verbose_name='障害', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.hurdle or ''


class Solution(models.Model):
    hurdle = models.ForeignKey(
        Hurdle, on_delete=models.CASCADE, related_name='solutions')
    solution_id = models.AutoField(primary_key=True)
    solution = models.TextField(verbose_name='解決策', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.solution or ''


class Document(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='documents')
    document_id = models.AutoField(primary_key=True)
    document_name = models.TextField(verbose_name='資料', null=True, blank=True)
    document_use = models.CharField(
        verbose_name='用途', null=True, blank=True, max_length=200)
    document_source = models.URLField(
        verbose_name='場所', null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.document_name or ''


class Discover(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='discovers')
    discover_id = models.AutoField(primary_key=True)
    discover_title = models.CharField(
        verbose_name='タイトル', null=True, blank=True, max_length=200)
    discover_main = models.TextField(
        verbose_name='本文', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='作成日時', default=timezone.now)
    update_at = models.DateTimeField(verbose_name='更新日時', default=timezone.now)
    first_hint = models.CharField(
        verbose_name='ヒント1', null=True, blank=True, max_length=20)
    second_hint = models.CharField(
        verbose_name='ヒント2', null=True, blank=True, max_length=20)
    third_hint = models.CharField(
        verbose_name='ヒント3', null=True, blank=True, max_length=20)

    def __str__(self):
        return self.discover_title or ''
