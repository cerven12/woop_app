# Generated by Django 3.0.5 on 2020-04-28 06:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('woop', '0015_auto_20200428_1205'),
    ]

    operations = [
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
    ]