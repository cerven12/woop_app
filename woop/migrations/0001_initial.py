# Generated by Django 3.0.5 on 2020-06-04 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('gift_id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('gift', models.CharField(max_length=150, verbose_name='ご褒美')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('goal_title', models.CharField(max_length=200, verbose_name='目標')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('goal_description', models.TextField(blank=True, null=True, verbose_name='詳細')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='開始日')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='締め切り')),
                ('achievement', models.IntegerField(blank=True, null=True, verbose_name='達成度')),
                ('progress_type', models.IntegerField(blank=True, choices=[(0, '一時停止'), (1, '挑戦中'), (2, '達成済')], null=True, verbose_name='進捗状況')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Worry',
            fields=[
                ('worry_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('worry', models.TextField(blank=True, null=True, verbose_name='心配事')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worries', to='woop.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=40, verbose_name='やること')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_repeat', models.BooleanField(default=False, verbose_name='繰り返し')),
                ('backup_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='woop.Task')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='woop.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='SelfTranscendenceGoal',
            fields=[
                ('selftrans_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('self_transcendence_goal', models.TextField(blank=True, null=True, verbose_name='自己超越目標')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='self_transcendence_goals', to='woop.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('reference_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='資料')),
                ('reference_use', models.CharField(blank=True, max_length=200, null=True, verbose_name='用途')),
                ('reference_source', models.URLField(blank=True, null=True, verbose_name='場所')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='woop.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='タイトル')),
                ('note_main', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='woop.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Motive',
            fields=[
                ('motive_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('motive', models.TextField(blank=True, null=True, verbose_name='動機')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motives', to='woop.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('idea_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('idea', models.TextField(blank=True, null=True, verbose_name='対策')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('worry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='woop.Worry')),
            ],
        ),
        migrations.CreateModel(
            name='FutureSelf',
            fields=[
                ('future_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('future_self', models.TextField(blank=True, null=True, verbose_name='将来の自分')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future_selves', to='woop.Goal')),
            ],
        ),
    ]
