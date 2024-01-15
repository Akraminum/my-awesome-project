from django.db import models
from model_utils.models import TimeStampedModel

from .goal import Goal


class Target(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_achieved = models.BooleanField(default=False)

    goal = models.ForeignKey(
        Goal,
        verbose_name="Target Goal",
        related_name="targets",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
