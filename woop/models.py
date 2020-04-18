from django.db import models
from django.utils import timezone

# Create your models here.
import uuid


class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='目標', max_length=40)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True,)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='やること', max_length=40)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title