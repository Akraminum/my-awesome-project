from django.db import models

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from .target import Target

class Task(TimeStampedModel):
    name = models.CharField(max_length=100)
    
    is_completed = models.BooleanField(default=False)
    date_completed = MonitorField(monitor='is_completed', when=[True], null=True)
    
    target = models.ForeignKey(
        Target,
        verbose_name="Task Target",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return self.name