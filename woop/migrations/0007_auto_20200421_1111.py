# Generated by Django 3.0.5 on 2020-04-21 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woop', '0006_auto_20200419_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='title',
            new_name='goal_title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='task_title',
        ),
    ]